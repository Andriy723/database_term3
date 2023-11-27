from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class PersonProfile(db.Model, IDto):
    __tablename__ = "person_profile"

    id_person_profile = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    birth_date = db.Column(db.String(10), nullable=True)
    follower_id_follower = db.Column(db.Integer, db.ForeignKey('follower.id_follower'))
    follower_creator_creator_id = db.Column(db.Integer, db.ForeignKey('follower.creator_creator_id'))

    follower = db.relationship("Follower", backref="person_profile")
    follower = db.relationship('Follower', foreign_keys=[follower_id_follower])
    follower = db.relationship('Follower', foreign_keys=[follower_creator_creator_id])

    def __repr__(self) -> str:
        return f"PersonProfile(id_person_profile={self.id_person_profile}, first_name={self.first_name}, " \
               f"last_name={self.last_name}, birth_date={self.birth_date}, " \
               f"follower_id_follower={self.follower_id_follower}, " \
               f"follower_creator_creator_id={self.follower_creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import follower_controller
        return {
            "id_person_profile": self.id_person_profile,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "follower_id_follower": follower_controller.find_by_id(self.follower_id_follower),
            "follower_creator_creator_id": follower_controller.find_by_id(self.follower_creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PersonProfile:
        obj = PersonProfile(
            id_person_profile=dto_dict.get("id_person_profile"),
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            birth_date=dto_dict.get("birth_date"),
            follower_id_follower=dto_dict.get("follower_id_follower"),
            follower_creator_creator_id=dto_dict.get("follower_creator_creator_id"),
        )
        return obj
