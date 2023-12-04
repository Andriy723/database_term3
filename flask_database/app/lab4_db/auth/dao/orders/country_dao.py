import sqlalchemy
from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import Country


class CountryDAO(GeneralDAO):

    _domain_type = Country

    def insert_country(self, city, current_place):
        self._session.execute(sqlalchemy.text("CALL InsertIntoCountries(:p1, :p2)"),
                              {"p1": city, "p2": current_place})
        self._session.commit()

    def insert_strings_countries(self, city, current_place):
        self._session.execute(sqlalchemy.text("CALL InsertStringsIntoCountries(:p1, :p2)"),
                              {"p1": city, "p2": current_place})
        self._session.commit()
