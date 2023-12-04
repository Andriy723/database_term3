from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import playlist_controller
from flask_database.app.lab4_db.auth.domain.orders.playlist import Playlist

playlist_bp = Blueprint('playlist', __name__, url_prefix='/playlist')


@playlist_bp.get('')
def get_all_playlist() -> Response:
    return make_response(jsonify(playlist_controller.find_all()), HTTPStatus.OK)


@playlist_bp.post('')
def create_playlist() -> Response:
    content = request.get_json()
    playlist = Playlist.create_from_dto(content)
    playlist_controller.create(playlist)
    return make_response(jsonify(playlist.put_into_dto()), HTTPStatus.CREATED)


@playlist_bp.get('/<int:playlist_id>')
def get_playlist(playlist_id: int) -> Response:
    return make_response(jsonify(playlist_controller.find_by_id(playlist_id)), HTTPStatus.OK)


@playlist_bp.put('/<int:playlist_id>')
def update_playlist(playlist_id: int) -> Response:
    content = request.get_json()
    playlist = Playlist.create_from_dto(content)
    playlist_controller.update(playlist_id, playlist)
    return make_response("Playlist updated", HTTPStatus.OK)


@playlist_bp.patch('/<int:playlist_id>')
def patch_playlist(playlist_id: int) -> Response:
    content = request.get_json()
    playlist_controller.patch(playlist_id, content)
    return make_response("Playlist updated", HTTPStatus.OK)


@playlist_bp.delete('/<int:playlist_id>')
def delete_playlist(playlist_id: int) -> Response:
    playlist_controller.delete(playlist_id)
    return make_response("Playlist deleted", HTTPStatus.OK)


@playlist_bp.get('/get-playlist-after-number/<int:in_num>')
def get_playlists_after_number(in_num: int) -> Response:

    return make_response(jsonify(playlist_controller.get_playlists_after_number(in_num)), HTTPStatus.OK)


@playlist_bp.get('/get-playlist-with-name/<string:name_filter>/after-number/<int:in_num>')
def get_playlists_with_name_and_number_filter(name_filter: str, in_num: int) -> Response:

    return make_response(jsonify(playlist_controller.get_playlists_with_name_and_number_filter(name_filter, in_num)),
                         HTTPStatus.OK)
