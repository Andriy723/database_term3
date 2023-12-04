from typing import List

from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import playlist_service


class PlaylistController(GeneralController):

    _service = playlist_service

    def get_playlists_after_number(self, in_number: int) -> List[object]:
        """
        Gets Client objects from database table with field 'number' >= in_number using Service layer as DTO objects.
        """
        return list(map(lambda x: dict(x), self._service.get_playlists_after_number(in_number)))

    def get_playlists_with_name_and_number_filter(self, name_filter: str, in_number: int) -> List[object]:
        """
        Gets Client objects from database table with name filter and field 'number' >= in_number
        """
        return list(map(lambda x: dict(x),
                        self._service.get_playlists_with_name_and_number_filter(name_filter, in_number)))

