from flask_database.app.lab4_db.auth.dao import country_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class CountryService(GeneralService):
    _dao = country_dao

    def insert_into_country(self, city, current_place):
        self._dao.insert_country(city, current_place)

    def insert_strings_country(self, city, current_place):
        self._dao.insert_strings_countries(city, current_place)
