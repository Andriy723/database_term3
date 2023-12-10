from flask_database.app.lab4_db.auth.dao import creator_has_music_labels_dao
from flask_database.app.lab4_db.auth.service.general_service import GeneralService


class CreatorHasMusicLabelsService(GeneralService):
    _dao = creator_has_music_labels_dao
