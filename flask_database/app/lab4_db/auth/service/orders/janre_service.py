from flask_database.app.lab4_db.auth.dao import janre_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class JanreService(GeneralService):
    _dao = janre_dao

    def create_db_name_janre(self):
        self._dao.create_db_name_janre()
