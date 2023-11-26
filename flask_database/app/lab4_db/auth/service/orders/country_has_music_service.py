from flask_database.app.lab4_db.auth.dao import country_has_music_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class CountryHasMusicService(GeneralService):
    _dao = country_has_music_dao
