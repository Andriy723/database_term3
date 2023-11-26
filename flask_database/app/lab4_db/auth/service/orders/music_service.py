from flask_database.app.lab4_db.auth.dao import music_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class MusicService(GeneralService):
    _dao = music_dao
