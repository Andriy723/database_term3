from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import country_service


class CountryController(GeneralController):

    _service = country_service
