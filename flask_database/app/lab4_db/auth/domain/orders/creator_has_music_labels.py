from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class CreatorHasMusicLabels(db.Model, IDto):
    __tablename__ = "creator_has_music_labels"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_creator_id = db.Column(db.Integer, db.ForeignKey('creator.creator_id'))
    music_labels_id_music_labels = db.Column(db.Integer, db.ForeignKey('music_labels.id_music_labels'))
    music_labels_creator_creator_id = db.Column(db.Integer, db.ForeignKey('music_labels.creator_creator_id'))

    creator = db.relationship("Creator", backref="creator_has_music_labels")
    music_labels = db.relationship("MusicLabels", backref="creator_has_music_labels")
    creator = db.relationship('Creator', foreign_keys=[creator_creator_id])
    music_labels = db.relationship('MusicLabels', foreign_keys=[music_labels_id_music_labels])
    music_labels = db.relationship('MusicLabels', foreign_keys=[music_labels_creator_creator_id])

    def __repr__(self) -> str:
        return f"CreatorHasMusicLabels(id={self.id}, " \
               f"creator_creator_id={self.creator_creator_id}, " \
               f"music_labels_id_music_labels={self.music_labels_id_music_labels}, " \
               f"music_labels_creator_creator_id={self.music_labels_creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import creator_controller
        from flask_database.app.lab4_db.auth.controller import music_labels_controller
        return {
            "id": self.id,
            "creator_creator_id": creator_controller.find_by_id(self.creator_creator_id),
            "music_labels_id_music_labels": music_labels_controller.find_by_id(self.music_labels_id_music_labels),
            "music_labels_creator_creator_id": music_labels_controller.find_by_id(self.music_labels_creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CreatorHasMusicLabels:
        obj = CreatorHasMusicLabels(
            id=dto_dict.get("id"),
            creator_creator_id=dto_dict.get("creator_creator_id"),
            music_labels_id_music_labels=dto_dict.get("music_labels_id_music_labels"),
            music_labels_creator_creator_id=dto_dict.get("music_labels_creator_creator_id"),
        )
        return obj
