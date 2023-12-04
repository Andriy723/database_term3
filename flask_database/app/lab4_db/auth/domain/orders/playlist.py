from __future__ import annotations

from cgitb import text
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class Playlist(db.Model, IDto):
    __tablename__ = "playlist"

    id_playlist = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'))

    def __repr__(self) -> str:
        return f"Playlist(id_playlist={self.id_playlist}, name={self.name}, " \
               f"music_id={self.music_id}, "

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import music_controller
        return {
            "id_playlist": self.id_playlist,
            "name": self.name,
            "music_id": music_controller.find_by_id(self.music_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Playlist:
        obj = Playlist(
            id_playlist=dto_dict.get("id_playlist"),
            name=dto_dict.get("name"),
            music_id=dto_dict.get("music_id"),
        )
        return obj

    @staticmethod
    def insert_into_playlist(name, music_id):
        sql = text("INSERT INTO playlist (name, music_id) VALUES (:name, :music_id)")
        db.engine.execute(sql, name=name, music_id=music_id)
