from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import music_service


class MusicController(GeneralController):

    _service = music_service
