from flask_database.app.lab4_db import db
from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import Music


class MusicDAO(GeneralDAO):

    _domain_type = Music

    @staticmethod
    def get_operations(operation):
        result = None

        if operation == 'MAX':
            result = db.session.query(db.func.max(Music.duration)).scalar()
        elif operation == 'MIN':
            result = db.session.query(db.func.min(Music.duration)).scalar()
        elif operation == 'SUM':
            result = db.session.query(db.func.sum(Music.duration)).scalar()
        elif operation == 'AVG':
            result = db.session.query(db.func.avg(Music.duration)).scalar()

        return result if result is not None else None

    @staticmethod
    def call_function_for_operations(operation):
        result = db.session.execute(
            "CALL FunctionForOperations(:operation)",
            {"operation": operation}
        )
        result = result.scalar()
        return result
