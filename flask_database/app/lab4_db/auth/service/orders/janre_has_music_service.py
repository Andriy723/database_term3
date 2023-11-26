from flask_database.app.lab4_db.auth.dao import janre_has_music_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class JanreHasMusicService(GeneralService):
    _dao = janre_has_music_dao
