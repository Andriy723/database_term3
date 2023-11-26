from flask_database.app.lab4_db.auth.dao import music_labels_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class MusicLabelsService(GeneralService):
    _dao = music_labels_dao
