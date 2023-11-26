from flask_database.app.lab4_db.auth.dao import albom_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class AlbomService(GeneralService):
    _dao = albom_dao
