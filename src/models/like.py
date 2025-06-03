from database.db import db 
from datetime import datetime


class Like(db.Model):  # Hereda de db.Model
    __tablename__ = "likes"

    LikeID = db.Column(db.Integer, primary_key=True, index=True)
    PostID = db.Column(db.Integer, db.ForeignKey(
        "posts.PostID"), nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey(
        "users.UserID"), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)

    post = db.relationship("Post", back_populates="likes")
    user = db.relationship("User", back_populates="likes")

    def __repr__(self):
        return f"<Like(LikeID={self.LikeID}, UserID={self.UserID}, PostID={self.PostID})>"
