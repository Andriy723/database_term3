from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import downloading_song_has_person_profile_service


class DownloadingSongHasPersonProfileController(GeneralController):

    _service = downloading_song_has_person_profile_service
