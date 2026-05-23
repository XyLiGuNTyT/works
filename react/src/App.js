import { useState, useEffect } from 'react';
import PostCard from './components/PostCard';
import './App.css';

function App() {
  const [posts, setPosts] = useState([]);
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchUsers = async () => {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/users');
      if (!response.ok) throw new Error('Ошибка загрузки пользователей');
      const data = await response.json();
      setUsers(data);
    } catch (err) {
      setError(err.message);
    }
  };

  const fetchPosts = async () => {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts');
      if (!response.ok) throw new Error('Ошибка загрузки постов');
      const data = await response.json();
      setPosts(data);
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      await Promise.all([fetchUsers(), fetchPosts()]);
      setLoading(false);
    };
    loadData();
  }, []);

  const getUserName = (userId) => {
    const user = users.find(u => u.id === userId);
    return user ? user.name : 'Неизвестный пользователь';
  };

  if (loading) {
    return <div className="loading">Загрузка постов...</div>;
  }

  if (error) {
    return <div className="error">Ошибка: {error}</div>;
  }

  return (
    <div className="app">
      <h1 className="app-title">Посты пользователей</h1>
      <div className="posts-grid">
        {posts.map(post => (
          <PostCard
            key={post.id}
            userName={getUserName(post.userId)}
            title={post.title}
            body={post.body}
          />
        ))}
      </div>
    </div>
  );
}

export default App;