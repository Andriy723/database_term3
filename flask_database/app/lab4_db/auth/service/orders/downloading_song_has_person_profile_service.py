from flask_database.app.lab4_db.auth.dao import downloading_song_has_person_profile_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class DownloadingSongHasPersonProfileService(GeneralService):
    _dao = downloading_song_has_person_profile_dao
