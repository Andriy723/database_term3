from flask_database.app.lab4_db.auth.dao.general_dao import GeneralDAO
from flask_database.app.lab4_db.auth.domain import Playlist
from typing import List
import sqlalchemy


class PlaylistDAO(GeneralDAO):

    _domain_type = Playlist

    def find_by_name(self, name: str) -> List[object]:

        return self._session.query(Playlist).filter(Playlist.name == name).order_by(Playlist.name).all()

    def find_by_number(self, number: int) -> List[object]:

        return self._session.query(Playlist).filter(Playlist.number == number).order_by(Playlist.number.desc()).all()

        # STORED PROCEDUREs
    def get_playlists_after_number(self, in_num: int) -> List[object]:

        return self._session.execute(sqlalchemy.text("CALL get_playlists_after_number(:p1)"),
                                     {"p1": in_num}).mappings().all()

    def get_playlists_with_name_and_number_filter(self, name_filter: str, in_num: int) -> List[object]:

        return self._session.execute(sqlalchemy.text("CALL get_playlists_with_name_and_number_filter(:p1, :p2)"),
                                     {"p1": name_filter, "p2": in_num}).mappings().all()

