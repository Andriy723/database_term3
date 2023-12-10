from flask_database.app.lab4_db.auth.dao import country_has_music_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class CountryHasMusicService(GeneralService):
    _dao = country_has_music_dao

    def insert_into_country_has_music(self, id_country, id_music):
        self._dao.insert_into_country_has_music(id_country, id_music)
