from flask_database.app.lab4_db.auth.dao import country_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class CountryService(GeneralService):
    _dao = country_dao
