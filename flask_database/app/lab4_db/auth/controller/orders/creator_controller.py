from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import creator_service


class CreatorController(GeneralController):

    _service = creator_service
