from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import music_labels_service


class MusicLabelsController(GeneralController):

    _service = music_labels_service
