from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class FollowerHasCreator(db.Model, IDto):
    __tablename__ = "follower_has_creator"

    follower_id_follower = db.Column(db.Integer, db.ForeignKey('follower.id_follower'), primary_key=True)
    follower_creator_creator_id = db.Column(db.Integer, db.ForeignKey('follower.creator_creator_id'), primary_key=True)
    creator_creator_id = db.Column(db.Integer, db.ForeignKey('creator.creator_id'), primary_key=True)

    follower = db.relationship("Follower", backref="follower_has_creator")
    creator = db.relationship("Creator", backref="follower_has_creator")

    def __repr__(self) -> str:
        return f"FollowerHasCreator(follower_id_follower={self.follower_id_follower}, " \
               f"follower_creator_creator_id={self.follower_creator_creator_id}, " \
               f"creator_creator_id={self.creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import follower_controller
        from flask_database.app.lab4_db.auth.controller import creator_controller
        return {
            "follower_id_follower": follower_controller.find_by_id(self.follower_id_follower),
            "follower_creator_creator_id": follower_controller.find_by_id(self.follower_creator_creator_id),
            "creator_creator_id": creator_controller.find_by_id(self.creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> FollowerHasCreator:
        obj = FollowerHasCreator(
            follower_id_follower=dto_dict.get("follower_id_follower"),
            follower_creator_creator_id=dto_dict.get("follower_creator_creator_id"),
            creator_creator_id=dto_dict.get("creator_creator_id"),
        )
        return obj
