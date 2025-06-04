from database.db import db
from datetime import datetime


class Follow(db.Model):  # Hereda de db.Model
    __tablename__ = "follows"

    follow_id = db.Column(db.Integer, primary_key=True, index=True)
    follower_user_id = db.Column(
        db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    following_user_id = db.Column(
        db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    follower = db.relationship(
        "User",
        foreign_keys=[follower_user_id],
        back_populates="following"
    )
    followed = db.relationship(
        "User",
        foreign_keys=[following_user_id],
        back_populates="followers"
    )

    def __repr__(self):
        return f"<Follow(follow_id={self.follow_id}, follower_user_id={self.follower_user_id}, following_user_id={self.following_user_id})>"
