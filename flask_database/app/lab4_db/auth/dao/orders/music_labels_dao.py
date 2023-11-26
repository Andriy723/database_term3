from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import MusicLabels


class MusicLabelsDAO(GeneralDAO):

    _domain_type = MusicLabels
