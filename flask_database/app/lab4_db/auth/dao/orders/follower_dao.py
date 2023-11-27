from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import Follower


class FollowerDAO(GeneralDAO):

    _domain_type = Follower
