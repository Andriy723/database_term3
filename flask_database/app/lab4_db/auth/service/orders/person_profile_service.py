from flask_database.app.lab4_db.auth.dao import person_profile_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class PersonProfileService(GeneralService):
    _dao = person_profile_dao
