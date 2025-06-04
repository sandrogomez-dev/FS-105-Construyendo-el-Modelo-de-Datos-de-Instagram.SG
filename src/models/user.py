from database.db import db 
from datetime import datetime


class User(db.Model):  
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(80), unique=True,
                         index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    
    posts = db.relationship(
        "Post", back_populates="author", cascade="all, delete-orphan")
    comments = db.relationship(
        "Comment", back_populates="author", cascade="all, delete-orphan")
    likes = db.relationship("Like", back_populates="user",
                            cascade="all, delete-orphan")

    following = db.relationship(
        "Follow",
        foreign_keys="[Follow.follower_user_id]",
        back_populates="follower",
        cascade="all, delete-orphan"
    )
    followers = db.relationship(
        "Follow",
        foreign_keys="[Follow.following_user_id]",
        back_populates="followed",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}')>"
