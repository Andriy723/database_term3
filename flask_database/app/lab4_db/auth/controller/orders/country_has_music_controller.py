from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import country_has_music_service


class CountryHasMusicController(GeneralController):

    _service = country_has_music_service
