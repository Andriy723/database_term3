from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class Country(db.Model, IDto):
    __tablename__ = "country"

    country_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(20), nullable=False)
    current_place = db.Column(db.String(25), nullable=False)

    def __repr__(self) -> str:
        return f"Country(country_id={self.country_id}, city={self.city}, current_place={self.current_place})"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "country_id": self.country_id,
            "city": self.city,
            "current_place": self.current_place,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Country:
        obj = Country(
            country_id=dto_dict.get("country_id"),
            city=dto_dict.get("city"),
            current_place=dto_dict.get("current_place"),
        )
        return obj
