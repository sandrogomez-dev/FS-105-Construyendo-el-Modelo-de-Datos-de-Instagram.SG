from database.db import db 
from datetime import datetime


class Post(db.Model):  
    __tablename__ = "posts"

    post_id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id"), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    author = db.relationship("User", back_populates="posts")
    comments = db.relationship(
        "Comment", back_populates="post", cascade="all, delete-orphan")
    likes = db.relationship("Like", back_populates="post",
                            cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Post(post_id={self.post_id}, user_id={self.user_id})>"
