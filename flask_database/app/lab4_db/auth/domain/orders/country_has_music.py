from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class CountryHasMusic(db.Model, IDto):
    __tablename__ = "country_has_music"

    id = db.Column(db.Integer, primary_key=True)
    country_country_id = db.Column(db.Integer, db.ForeignKey('country.country_id'))
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'))
    music_albom_id_albom = db.Column(db.Integer, db.ForeignKey('music.albom_id_albom'))
    price = db.Column(db.String(20), nullable=True)
    price_curency = db.Column(db.String(20), nullable=True)

    country = db.relationship("Country", backref="country_has_music")
    music = db.relationship("Music", backref="country_has_music")
    country = db.relationship('Country', foreign_keys=[country_country_id])
    music = db.relationship('Music', foreign_keys=[music_id])
    music = db.relationship('Music', foreign_keys=[music_albom_id_albom])

    def __repr__(self) -> str:
        return f"CountryHasMusic(id={self.id}, music_id={self.music_id}, " \
               f"country_country_id={self.country_country_id}, " \
               f"music_albom_id_albom={self.music_albom_id_albom}, price={self.price}, " \
               f"price_curency={self.price_curency})"

    def put_into_dto(self) -> Dict[str, Any]:
        from flask_database.app.lab4_db.auth.controller import country_controller
        from flask_database.app.lab4_db.auth.controller import music_controller
        return {
            "id": self.id,
            "country_country_id": country_controller.find_by_id(self.country_country_id),
            "music_id": music_controller.find_by_id(self.music_id),
            "music_albom_id_albom": music_controller.find_by_id(self.music_albom_id_albom),
            "price": self.price,
            "price_curency": self.price_curency,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CountryHasMusic:
        obj = CountryHasMusic(
            id=dto_dict.get("id"),
            country_country_id=dto_dict.get("country_country_id"),
            music_id=dto_dict.get("music_id"),
            music_albom_id_albom=dto_dict.get("music_albom_id_albom"),
            price=dto_dict.get("price"),
            price_curency=dto_dict.get("price_curency"),
        )
        return obj
