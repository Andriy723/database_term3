from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import country_service


class CountryController(GeneralController):

    _service = country_service

    def insert_into_country_parameters(self, city, current_place):
        self._service.insert_into_country(city, current_place)

    def insert_strings_country_parameters(self, city, current_place):
        self._service.insert_strings_country(city, current_place)
