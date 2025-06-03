from database.db import db
from datetime import datetime


class Follow(db.Model):  # Hereda de db.Model
    __tablename__ = "follows"

    FollowID = db.Column(db.Integer, primary_key=True, index=True)
    FollowerUserID = db.Column(
        db.Integer, db.ForeignKey("users.UserID"), nullable=False)
    FollowingUserID = db.Column(
        db.Integer, db.ForeignKey("users.UserID"), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.utcnow)

    follower = db.relationship(
        "User",
        foreign_keys=[FollowerUserID],
        back_populates="following"
    )
    followed = db.relationship(
        "User",
        foreign_keys=[FollowingUserID],
        back_populates="followers"
    )

    def __repr__(self):
        return f"<Follow(FollowID={self.FollowID}, FollowerUserID={self.FollowerUserID}, FollowingUserID={self.FollowingUserID})>"
