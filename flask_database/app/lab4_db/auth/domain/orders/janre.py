from __future__ import annotations
from typing import Dict, Any
from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.domain.i_dto import IDto


class Janre(db.Model, IDto):
    __tablename__ = "janre"

    janre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"Janre(janre_id={self.janre_id}, name={self.name})"

    def put_into_dto(self) -> Dict[str, Any]:

        return {
            "janre_id": self.janre_id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Janre:
        obj = Janre(
            janre_id=dto_dict.get("janre_id"),
            name=dto_dict.get("name"),
        )
        return obj
