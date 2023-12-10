from flask_database.app.lab4_db.auth.dao import music_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class MusicService(GeneralService):
    _dao = music_dao

    @staticmethod
    def get_operations(operation):
        return music_dao.get_operations(operation)

    @staticmethod
    def call_function_for_operations(operation):
        return music_dao.call_function_for_operations(operation)
