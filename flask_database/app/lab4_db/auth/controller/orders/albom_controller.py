from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import albom_service


class AlbomController(GeneralController):

    _service = albom_service
