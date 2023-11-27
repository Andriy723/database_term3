from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import creator_has_music_labels_service


class CreatorHasMusicLabelsController(GeneralController):

    _service = creator_has_music_labels_service
