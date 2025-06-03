from src.database.db import db
from datetime import datetime


class User(db.Model):  # Hereda de db.Model de Flask-SQLAlchemy
    __tablename__ = "users"

    UserID = db.Column(db.Integer, primary_key=True, index=True)
    Username = db.Column(db.String(80), unique=True,
                         index=True, nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    PasswordHash = db.Column(db.String(255), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones:
    # Usamos db.relationship y el nombre de la clase del modelo directamente
    posts = db.relationship(
        "Post", back_populates="author", cascade="all, delete-orphan")
    comments = db.relationship(
        "Comment", back_populates="author", cascade="all, delete-orphan")
    likes = db.relationship("Like", back_populates="user",
                            cascade="all, delete-orphan")

    # Relaciones de seguimiento (Follow):
    following = db.relationship(
        "Follow",
        foreign_keys="[Follow.FollowerUserID]",
        back_populates="follower",
        cascade="all, delete-orphan"
    )
    followers = db.relationship(
        "Follow",
        foreign_keys="[Follow.FollowingUserID]",
        back_populates="followed",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(UserID={self.UserID}, Username='{self.Username}')>"
