from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class MusicLabels(db.Model, IDto):
    __tablename__ = "music_labels"

    id_music_labels = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label_name = db.Column(db.String(25), nullable=False)
    creator_creator_id = db.Column(db.Integer, db.ForeignKey('creator.creator_id'), nullable=False)

    def __repr__(self) -> str:
        return f"MusicLabels(id_music_labels={self.id_music_labels}, label_name={self.label_name}, " \
               f"creator_creator_id={self.creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import creator_controller
        return {
            "id_music_labels": self.id_music_labels,
            "label_name": self.label_name,
            # "creator_creator_id": creator_controller.find_by_id(self.creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MusicLabels:
        obj = MusicLabels(
            id_music_labels=dto_dict.get("id_music_labels"),
            label_name=dto_dict.get("label_name"),
            creator_creator_id=dto_dict.get("creator_creator_id"),
        )
        return obj
