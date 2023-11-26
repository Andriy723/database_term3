from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import downloading_song_controller
from flask_database.app.lab4_db.auth.domain.orders.downloading_song import DownloadingSong

downloading_song_bp = Blueprint('downloading_song', __name__, url_prefix='/downloading_song')


@downloading_song_bp.get('')
def get_all_downloading_song() -> Response:
    return make_response(jsonify(downloading_song_controller.find_all()), HTTPStatus.OK)


@downloading_song_bp.post('')
def create_downloading_song() -> Response:
    content = request.get_json()
    downloading_song = DownloadingSong.create_from_dto(content)
    downloading_song_controller.create(downloading_song)
    return make_response(jsonify(downloading_song.put_into_dto()), HTTPStatus.CREATED)


@downloading_song_bp.get('/<int:downloading_song_id>')
def get_downloading_song(downloading_song_id: int) -> Response:
    return make_response(jsonify(downloading_song_controller.
                                 find_by_id(downloading_song_id)), HTTPStatus.OK)


@downloading_song_bp.put('/<int:downloading_song_id>')
def update_downloading_song(downloading_song_id: int) -> Response:
    content = request.get_json()
    downloading_song = DownloadingSong.create_from_dto(content)
    downloading_song_controller.update(downloading_song_id, downloading_song)
    return make_response("Downloading_song updated", HTTPStatus.OK)


@downloading_song_bp.patch('/<int:downloading_song_id>')
def patch_downloading_song(downloading_song_id: int) -> Response:
    content = request.get_json()
    downloading_song_controller.patch(downloading_song_id, content)
    return make_response("Downloading_song updated", HTTPStatus.OK)


@downloading_song_bp.delete('/<int:downloading_song_id>')
def delete_downloading_song(downloading_song_id: int) -> Response:
    downloading_song_controller.delete(downloading_song_id)
    return make_response("Downloading_song deleted", HTTPStatus.OK)
