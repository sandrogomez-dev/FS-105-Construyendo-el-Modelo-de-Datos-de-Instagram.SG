from database.db import db 
from datetime import datetime


class Like(db.Model):  
    __tablename__ = "likes"

    like_id = db.Column(db.Integer, primary_key=True, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        "posts.post_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    post = db.relationship("Post", back_populates="likes")
    user = db.relationship("User", back_populates="likes")

    def __repr__(self):
        return f"<Like(like_id={self.like_id}, user_id={self.user_id}, post_id={self.post_id})>"
