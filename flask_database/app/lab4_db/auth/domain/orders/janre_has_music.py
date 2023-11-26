from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class JanreHasMusic(db.Model, IDto):
    __tablename__ = "janre_has_music"

    janre_janre_id = db.Column(db.Integer, db.ForeignKey('janre.janre_id'), primary_key=True)
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'), primary_key=True)
    music_albom_id_albom = db.Column(db.Integer, db.ForeignKey('music.albom_id_albom'), primary_key=True)
    music_creator_creator_id = db.Column(db.Integer, db.ForeignKey('music.creator_creator_id'), primary_key=True)

    janre = db.relationship("Janre", backref="janre_has_music")
    music = db.relationship("Music", backref="janre_has_music")

    def __repr__(self) -> str:
        return f"JanreHasMusic(janre_janre_id={self.janre_janre_id}, music_id={self.music_id}, " \
               f"music_albom_id_albom={self.music_albom_id_albom}, " \
               f"music_creator_creator_id={self.music_creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import music_controller
        from flask_database.app.lab4_db.auth.controller import janre_controller
        return {
            "janre_janre_id": janre_controller.find_by_id(self.janre_janre_id),
            "music_id": music_controller.find_by_id(self.music_id),
            "music_albom_id_albom": music_controller.find_by_id(self.music_albom_id_albom),
            "music_creator_creator_id":music_controller.find_by_id(self.music_creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> JanreHasMusic:
        obj = JanreHasMusic(
            janre_janre_id=dto_dict.get("janre_janre_id"),
            music_id=dto_dict.get("music_id"),
            music_albom_id_albom=dto_dict.get("music_albom_id_albom"),
            music_creator_creator_id=dto_dict.get("music_creator_creator_id"),
        )
        return obj
