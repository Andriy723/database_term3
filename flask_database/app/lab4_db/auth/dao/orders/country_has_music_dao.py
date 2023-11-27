from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import CountryHasMusic


class CountryHasMusicDAO(GeneralDAO):

    _domain_type = CountryHasMusic
