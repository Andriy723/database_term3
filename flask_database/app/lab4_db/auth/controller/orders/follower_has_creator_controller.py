from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import follower_has_creator_service


class FollowerHasCreatorController(GeneralController):

    _service = follower_has_creator_service
