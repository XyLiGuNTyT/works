from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models import Q
from .models import News, Comment
from .forms import NewsForm, CommentForm

def home(request):
    latest_news = News.objects.all()[:3]
    return render(request, 'news/home.html', {'latest_news': latest_news})

def contacts(request):
    return render(request, 'news/contacts.html')

def news_list(request):
    news_queryset = News.objects.all()
    search_query = request.GET.get('search', '')
    sort = request.GET.get('sort', 'desc')
    if search_query:
        news_queryset = news_queryset.filter(Q(title__icontains=search_query))
    if sort == 'asc':
        news_queryset = news_queryset.order_by('pub_date')
    else:
        news_queryset = news_queryset.order_by('-pub_date')
    return render(request, 'news/news_list.html', {
        'news_list': news_queryset,
        'search_query': search_query,
        'sort': sort,
    })

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    comments = news.comments.filter(is_approved=True)
    form = CommentForm()  # пустая форма для GET
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.author = request.user
            comment.save()
            return redirect('news_detail', pk=pk)
        # если форма невалидна, останется с ошибками
    return render(request, 'news/news_detail.html', {
        'news': news,
        'comments': comments,
        'form': form,
    })

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'news/register.html'
    success_url = reverse_lazy('login')

@login_required
def profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    comments = request.user.comment_set.all()  
    return render(request, 'news/profile.html', {'form': form, 'comments': comments})

@staff_member_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form, 'title': 'Создание новости'})

@staff_member_required
def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_form.html', {'form': form, 'title': 'Редактирование новости'})

@staff_member_required
def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'news/news_confirm_delete.html', {'news': news})