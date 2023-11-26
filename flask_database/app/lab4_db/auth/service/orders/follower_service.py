from flask_database.app.lab4_db.auth.dao import follower_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class FollowerService(GeneralService):
    _dao = follower_dao
