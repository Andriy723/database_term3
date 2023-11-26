from flask_database.app.lab4_db.auth.dao import creator_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class CreatorService(GeneralService):
    _dao = creator_dao
