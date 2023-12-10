import sqlalchemy
from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import CountryHasMusic


class CountryHasMusicDAO(GeneralDAO):

    _domain_type = CountryHasMusic

    def insert_into_country_has_music(self, id_country, id_music):
        self._session.execute(sqlalchemy.text("CALL InsertIntoCountryHasMusic(:p1, :p2)"),
                              {"p1": id_country, "p2": id_music})
        self._session.commit()
