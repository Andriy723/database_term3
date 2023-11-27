from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import downloading_song_service


class DownloadingSongController(GeneralController):

    _service = downloading_song_service
