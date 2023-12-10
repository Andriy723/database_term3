from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import follower_service


class FollowerController(GeneralController):

    _service = follower_service
