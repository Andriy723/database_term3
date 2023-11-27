from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class Music(db.Model, IDto):
    __tablename__ = "music"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    duration = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(40), nullable=False)
    albom_id_albom = db.Column(db.Integer, db.ForeignKey('albom.id_albom'))
    creator_creator_id = db.Column(db.Integer, db.ForeignKey('creator.creator_id'))

    albom = db.relationship("Albom", backref="music")
    creator = db.relationship("Creator", backref="music")

    def __repr__(self) -> str:
        return f"Music(id={self.id}, duration={self.duration}, name={self.name}, " \
               f"albom_id_albom={self.albom_id_albom}, creator_creator_id={self.creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import albom_controller
        from flask_database.app.lab4_db.auth.controller import creator_controller
        return {
            "id": self.id,
            "duration": self.duration,
            "name": self.name,
            "albom_id_albom": albom_controller.find_by_id(self.albom_id_albom),
            "creator_creator_id": creator_controller.find_by_id(self.creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Music:
        obj = Music(
            id=dto_dict.get("id"),
            duration=dto_dict.get("duration"),
            name=dto_dict.get("name"),
            albom_id_albom=dto_dict.get("albom_id_albom"),
            creator_creator_id=dto_dict.get("creator_creator_id"),
        )
        return obj
