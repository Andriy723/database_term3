from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class Albom(db.Model, IDto):
    __tablename__ = "albom"

    id_albom = db.Column(db.Integer, primary_key=True, autoincrement=True)
    songs_num = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    creator_creator_id = db.Column(db.Integer, db.ForeignKey('creator.creator_id'))
    music_labels_id_music_labels = db.Column(db.Integer, db.ForeignKey('music_labels.id_music_labels'))
    music_labels_creator_creator_id = db.Column(db.Integer, db.ForeignKey('music_labels.creator_creator_id'))

    creator = db.relationship("Creator", backref="albom")
    music_labels = db.relationship("MusicLabels", backref="albom")

    def __repr__(self) -> str:
        return f"Albom(id_albom={self.id_albom}, songs_num={self.songs_num}, name={self.name}, " \
               f"creator_creator_id={self.creator_creator_id}, " \
               f"music_labels_id_music_labels={self.music_labels_id_music_labels}, " \
               f"music_labels_creator_creator_id={self.music_labels_creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import creator_controller
        from flask_database.app.lab4_db.auth.controller import music_labels_controller
        return {
            "id_albom": self.id_albom,
            "songs_num": self.songs_num,
            "name": self.name,
            "creator_creator_id": creator_controller.find_by_id(self.creator_creator_id),
            "music_labels_id_music_labels": music_labels_controller.find_by_id(self.music_labels_id_music_labels),
            "music_labels_creator_creator_id": music_labels_controller.find_by_id(self.music_labels_creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Albom:
        obj = Albom(
            id_albom=dto_dict.get("id_albom"),
            songs_num=dto_dict.get("songs_num"),
            name=dto_dict.get("name"),
            creator_creator_id=dto_dict.get("creator_creator_id"),
            music_labels_id_music_labels=dto_dict.get("music_labels_id_music_labels"),
            music_labels_creator_creator_id=dto_dict.get("music_labels_creator_creator_id"),
        )
        return obj
