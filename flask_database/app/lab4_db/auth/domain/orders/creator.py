from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class Creator(db.Model, IDto):
    __tablename__ = "creator"

    creator_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    birth_date = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"Creator(creator_id={self.creator_id}, first_name={self.first_name}, " \
               f"last_name={self.last_name}, birth_date={self.birth_date})"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "creator_id": self.creator_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Creator:
        obj = Creator(
            creator_id=dto_dict.get("creator_id"),
            first_name=dto_dict.get("first_name"),
            last_name=dto_dict.get("last_name"),
            birth_date=dto_dict.get("birth_date"),
        )
        return obj
