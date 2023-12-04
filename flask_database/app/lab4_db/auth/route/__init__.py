from flask import Flask
from flask_database.app.lab4_db.auth.route.error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)

    from .orders.albom_route import albom_bp
    app.register_blueprint(albom_bp)
    from .orders.country_route import country_bp
    app.register_blueprint(country_bp)
    from .orders.country_has_music_route import country_has_music_bp
    app.register_blueprint(country_has_music_bp)
    from .orders.creator_route import creator_bp
    app.register_blueprint(creator_bp)
    from .orders.creator_has_music_labels_route import creator_has_music_labels_bp
    app.register_blueprint(creator_has_music_labels_bp)
    from .orders.downloading_song_route import downloading_song_bp
    app.register_blueprint(downloading_song_bp)
    from .orders.downloading_song_has_person_profile_route import downloading_song_has_person_profile_bp
    app.register_blueprint(downloading_song_has_person_profile_bp)
    from .orders.follower_route import follower_bp
    app.register_blueprint(follower_bp)
    from .orders.follower_has_creator_route import follower_has_creator_bp
    app.register_blueprint(follower_has_creator_bp)
    from .orders.janre_route import janre_bp
    app.register_blueprint(janre_bp)
    from .orders.janre_has_music_route import janre_has_music_bp
    app.register_blueprint(janre_has_music_bp)
    from .orders.music_route import music_bp
    app.register_blueprint(music_bp)
    from .orders.music_labels_route import music_labels_bp
    app.register_blueprint(music_labels_bp)
    from .orders.person_profile_route import person_profile_bp
    app.register_blueprint(person_profile_bp)
    from .orders.playlist_route import playlist_bp
    app.register_blueprint(playlist_bp)
    