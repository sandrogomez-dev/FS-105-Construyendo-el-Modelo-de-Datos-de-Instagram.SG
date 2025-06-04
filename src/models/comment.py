from database.db import db
from datetime import datetime


class Comment(db.Model):  
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        "posts.post_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id"), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    post = db.relationship("Post", back_populates="comments")
    author = db.relationship("User", back_populates="comments")

    def __repr__(self):
        return f"<Comment(comment_id={self.comment_id}, user_id={self.user_id}, post_id={self.post_id})>"
