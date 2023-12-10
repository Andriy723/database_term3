from typing import List
from flask_database.app.lab4_db.auth.dao import playlist_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class PlaylistService(GeneralService):
    _dao = playlist_dao

    def get_playlists_s_after_number(self, in_number: int) -> List[object]:
        """
        Gets Client objects from database table with field 'number' >= in_number.
        :param in_number: number value
        :return: list of all objects
        """
        return self._dao.get_playlists_s_after_number(in_number)

    def get_playlists_with_name_and_number_filter(self, name_filter: str, in_number: int) -> List[object]:
        """
        Gets Client objects from database table with name filter and field 'number' >= in_number.
        :param name_filter: first letters of name
        :param in_number: number value
        :return: list of all objects
        """
        return self._dao.get_playlists_with_name_and_number_filter(name_filter, in_number)
