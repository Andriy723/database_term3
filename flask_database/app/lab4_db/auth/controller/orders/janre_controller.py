from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import janre_service


class JanreController(GeneralController):

    _service = janre_service

    def create_db_name_janre(self):
        self._service.create_db_name_janre()
