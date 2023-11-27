from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class DownloadingSongHasPersonProfile(db.Model, IDto):
    __tablename__ = "downloading_song_has_person_profile"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    downloading_song_id_downloading_song = db.Column(
        db.Integer, db.ForeignKey('downloading_song.id_downloading_song'))
    downloading_song_music_id = db.Column(
        db.Integer, db.ForeignKey('downloading_song.music_id'))
    downloading_song_music_albom_id_albom = db.Column(
        db.Integer, db.ForeignKey('downloading_song.music_albom_id_albom'))
    person_profile_id_person_profile = db.Column(
        db.Integer, db.ForeignKey('person_profile.id_person_profile'))
    person_profile_follower_id_follower = db.Column(
        db.Integer, db.ForeignKey('person_profile.follower_id_follower'))
    person_profile_follower_creator_creator_id = db.Column(
        db.Integer, db.ForeignKey('person_profile.follower_creator_creator_id'))

    downloading_song = db.relationship("DownloadingSong", backref="downloading_song_has_person_profile")
    person_profile = db.relationship("PersonProfile", backref="downloading_song_has_person_profile")
    downloading_song = db.relationship('DownloadingSong', foreign_keys=[downloading_song_id_downloading_song])
    downloading_song = db.relationship('DownloadingSong', foreign_keys=[downloading_song_music_id])
    downloading_song = db.relationship('DownloadingSong', foreign_keys=[downloading_song_music_albom_id_albom])
    person_profile = db.relationship('PersonProfile', foreign_keys=[person_profile_id_person_profile])
    person_profile = db.relationship('PersonProfile', foreign_keys=[person_profile_follower_id_follower])
    person_profile = db.relationship('PersonProfile', foreign_keys=[person_profile_follower_creator_creator_id])

    def __repr__(self) -> str:
        return f"DownloadingSongHasPersonProfile(id=" \
               f"{self.id}, " \
               f", downloading_song_id_downloading_song=" \
               f"{self.downloading_song_id_downloading_song}, " \
               f"downloading_song_music_id={self.downloading_song_music_id}, " \
               f"downloading_song_music_albom_id_albom={self.downloading_song_music_albom_id_albom}, " \
               f"person_profile_id_person_profile={self.person_profile_id_person_profile}, " \
               f"person_profile_follower_id_follower={self.person_profile_follower_id_follower}, " \
               f"person_profile_follower_creator_creator_id={self.person_profile_follower_creator_creator_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import downloading_song_controller
        from flask_database.app.lab4_db.auth.controller import person_profile_controller
        return {
            "id": self.id,
            "downloading_song_id_downloading_song": downloading_song_controller.find_by_id(
                self.downloading_song_id_downloading_song),
            "downloading_song_music_id": downloading_song_controller.find_by_id(
                self.downloading_song_music_id),
            "downloading_song_music_albom_id_albom": downloading_song_controller.find_by_id(
                self.downloading_song_music_albom_id_albom),
            "person_profile_id_person_profile": person_profile_controller.find_by_id(
                self.person_profile_id_person_profile),
            "person_profile_follower_id_follower": person_profile_controller.find_by_id(
                self.person_profile_follower_id_follower),
            "person_profile_follower_creator_creator_id": person_profile_controller.find_by_id(
                self.person_profile_follower_creator_creator_id),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DownloadingSongHasPersonProfile:
        obj = DownloadingSongHasPersonProfile(
            id=dto_dict.get("id"),
            downloading_song_id_downloading_song=dto_dict.get("downloading_song_id_downloading_song"),
            downloading_song_music_id=dto_dict.get("downloading_song_music_id"),
            downloading_song_music_albom_id_albom=dto_dict.get("downloading_song_music_albom_id_albom"),
            person_profile_id_person_profile=dto_dict.get("person_profile_id_person_profile"),
            person_profile_follower_id_follower=dto_dict.get("person_profile_follower_id_follower"),
            person_profile_follower_creator_creator_id=dto_dict.get("person_profile_follower_creator_creator_id"),
        )
        return obj
