import './PostCard.css';

function PostCard({ userName, title, body }) {
  return (
    <div className="post-card">
      <div className="card-header">
        {userName}
      </div>
      <div className="card-body">
        <h3 className="post-title">{title}</h3>
        <p className="post-body">{body}</p>
      </div>
    </div>
  );
}

export default PostCard;