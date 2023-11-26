from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import Janre


class JanreDAO(GeneralDAO):

    _domain_type = Janre
