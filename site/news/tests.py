from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import News, Comment

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_news_creation(self):
        """Проверка создания новости"""
        news = News.objects.create(
            title='Заголовок',
            content='Содержание новости',
            author=self.user
        )
        self.assertEqual(news.title, 'Заголовок')
        self.assertEqual(str(news), 'Заголовок')
        self.assertIsNotNone(news.pub_date)

    def test_comment_creation(self):
        """Проверка создания комментария"""
        news = News.objects.create(title='Новость', content='Текст', author=self.user)
        comment = Comment.objects.create(
            news=news,
            author=self.user,
            text='Отличная новость!',
            is_approved=True
        )
        self.assertEqual(comment.text, 'Отличная новость!')
        self.assertEqual(comment.news.title, 'Новость')
        self.assertTrue(comment.is_approved)

    def test_comment_has_required_fields(self):
        """Проверка наличия всех необходимых полей в модели Comment"""
        fields = [f.name for f in Comment._meta.get_fields()]
        required_fields = ['news', 'author', 'text', 'created_date', 'is_approved']
        for field in required_fields:
            self.assertIn(field, fields)


class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='viewer', password='pass')
        self.news = News.objects.create(
            title='Тестовая новость',
            content='Содержание для теста',
            author=self.user
        )

    def test_home_page_status(self):
        """Главная страница доступна"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_page_status(self):
        """Страница контактов доступна"""
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)

    def test_news_list_page_status(self):
        """Страница списка новостей доступна"""
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)

    def test_news_detail_page_status(self):
        """Страница отдельной новости доступна"""
        response = self.client.get(reverse('news_detail', args=[self.news.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая новость')

    def test_news_list_search(self):
        """Проверка поиска новостей по заголовку"""
        News.objects.create(title='Python новости', content='...', author=self.user)
        News.objects.create(title='Django уроки', content='...', author=self.user)
        response = self.client.get(reverse('news_list') + '?search=Python')
        self.assertContains(response, 'Python новости')
        self.assertNotContains(response, 'Django уроки')

    def test_news_list_sorting(self):
        """Проверка сортировки новостей по дате"""
        from django.utils import timezone
        import datetime
        news1 = News.objects.create(title='Старая', content='...', author=self.user, pub_date=timezone.now() - datetime.timedelta(days=5))
        news2 = News.objects.create(title='Новая', content='...', author=self.user, pub_date=timezone.now())
        # Сортировка по умолчанию (новые сверху)
        response = self.client.get(reverse('news_list'))
        content = response.content.decode()
        idx_new = content.find('Новая')
        idx_old = content.find('Старая')
        self.assertLess(idx_new, idx_old)  # Новая должна быть раньше
        # Сортировка asc (старые сверху)
        response = self.client.get(reverse('news_list') + '?sort=asc')
        content = response.content.decode()
        idx_new = content.find('Новая')
        idx_old = content.find('Старая')
        self.assertGreater(idx_new, idx_old)  # Старая должна быть раньше


class AuthTestCase(TestCase):
    def test_user_registration(self):
        """Проверка регистрации нового пользователя"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })
        self.assertEqual(response.status_code, 302)  # редирект после регистрации
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        """Проверка входа пользователя"""
        User.objects.create_user(username='loguser', password='secret')
        response = self.client.post(reverse('login'), {
            'username': 'loguser',
            'password': 'secret',
        })
        self.assertEqual(response.status_code, 302)  # редирект после входа
        self.assertIn('_auth_user_id', self.client.session)

    def test_user_logout(self):
        """Проверка выхода пользователя"""
        self.client.login(username='loguser', password='secret')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)


class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='commenter', password='pass')
        self.news = News.objects.create(
            title='Новость для комментариев',
            content='Контент',
            author=self.user
        )

    def test_authenticated_user_can_comment(self):
        """Авторизованный пользователь может оставить комментарий"""
        self.client.login(username='commenter', password='pass')
        response = self.client.post(reverse('news_detail', args=[self.news.pk]), {
            'text': 'Мой тестовый комментарий'
        })
        self.assertEqual(response.status_code, 302)  # редирект после успешного добавления
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.text, 'Мой тестовый комментарий')
        self.assertEqual(comment.author, self.user)

    def test_unauthenticated_user_cannot_comment(self):
        """Неавторизованный пользователь не может оставить комментарий"""
        response = self.client.post(reverse('news_detail', args=[self.news.pk]), {
            'text': 'Попытка комментария без логина'
        })
        # Должен быть редирект на страницу входа или 302, но комментарий не создаётся
        self.assertEqual(Comment.objects.count(), 0)