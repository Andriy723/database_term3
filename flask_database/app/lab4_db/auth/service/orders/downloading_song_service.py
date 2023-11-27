from flask_database.app.lab4_db.auth.dao import downloading_song_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class DownloadingSongService(GeneralService):
    _dao = downloading_song_dao
