from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import janre_has_music_service


class JanreHasMusicController(GeneralController):

    _service = janre_has_music_service
