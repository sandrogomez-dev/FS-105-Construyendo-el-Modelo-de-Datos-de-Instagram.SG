from database.db import db
from datetime import datetime


class Comment(db.Model):  # Hereda de db.Model
    __tablename__ = "comments"

    CommentID = db.Column(db.Integer, primary_key=True, index=True)
    PostID = db.Column(db.Integer, db.ForeignKey(
        "posts.PostID"), nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey(
        "users.UserID"), nullable=False)
    Content = db.Column(db.String(500), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)

    post = db.relationship("Post", back_populates="comments")
    author = db.relationship("User", back_populates="comments")

    def __repr__(self):
        return f"<Comment(CommentID={self.CommentID}, UserID={self.UserID}, PostID={self.PostID})>"
