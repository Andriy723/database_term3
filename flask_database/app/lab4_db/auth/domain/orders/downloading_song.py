from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class DownloadingSong(db.Model, IDto):
    __tablename__ = "downloading_song"

    id_downloading_song = db.Column(db.Integer, primary_key=True, autoincrement=True)
    downloading_num = db.Column(db.Integer, nullable=True)
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'))
    music_albom_id_albom = db.Column(db.Integer, db.ForeignKey('music.albom_id_albom'))

    music = db.relationship("Music", backref="downloading_song")
    music = db.relationship('Music', foreign_keys=[music_id])
    music = db.relationship('Music', foreign_keys=[music_albom_id_albom])

    def __repr__(self) -> str:
        return f"DownloadingSong(id_downloading_song={self.id_downloading_song}, " \
               f"downloading_num={self.downloading_num}, " \
               f"music_id={self.music_id}, " \
               f"music_albom_id_albom={self.music_albom_id_albom})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import music_controller
        return {
            "id_downloading_song": self.id_downloading_song,
            "downloading_num": self.downloading_num,
            "music_id": music_controller.find_by_id(self.music_id),
            "music_albom_id_albom": music_controller.find_by_id(self.music_albom_id_albom),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DownloadingSong:
        obj = DownloadingSong(
            id_downloading_song=dto_dict.get("id_downloading_song"),
            downloading_num=dto_dict.get("downloading_num"),
            music_id=dto_dict.get("music_id"),
            music_albom_id_albom=dto_dict.get("music_albom_id_albom"),
        )
        return obj
