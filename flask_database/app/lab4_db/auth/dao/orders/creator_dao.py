from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import Creator


class CreatorDAO(GeneralDAO):

    _domain_type = Creator
