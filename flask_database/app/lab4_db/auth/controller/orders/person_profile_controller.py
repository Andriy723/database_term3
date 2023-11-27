from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import person_profile_service


class PersonProfileController(GeneralController):

    _service = person_profile_service
