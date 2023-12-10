from flask_database.app.lab4_db.auth.dao import follower_has_creator_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class FollowerHasCreatorService(GeneralService):
    _dao = follower_has_creator_dao
