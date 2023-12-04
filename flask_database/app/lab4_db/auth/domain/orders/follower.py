from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class Follower(db.Model, IDto):
    __tablename__ = "follower"

    id_follower = db.Column(db.Integer, primary_key=True, autoincrement=True)
    followers_num = db.Column(db.Integer, nullable=True)
    creator_creator_id = db.Column(db.Integer, db.ForeignKey('creator.creator_id'), nullable=False)

    def __repr__(self) -> str:
        return f"Follower(id_follower={self.id_follower}, followers_num={self.followers_num}, " \
               f"creator_creator_id={self.creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        # from flask_database.app.lab4_db.auth.controller import creator_controller
        return {
            "id_follower": self.id_follower,
            "followers_num": self.followers_num,
            # "creator_creator_id": creator_controller.find_by_id(self.creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Follower:
        obj = Follower(
            id_follower=dto_dict.get("id_follower"),
            followers_num=dto_dict.get("followers_num"),
            creator_creator_id=dto_dict.get("creator_creator_id"),
        )
        return obj
