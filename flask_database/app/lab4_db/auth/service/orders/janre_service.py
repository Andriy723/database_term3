from flask_database.app.lab4_db.auth.dao import janre_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class JanreService(GeneralService):
    _dao = janre_dao
