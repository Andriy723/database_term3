from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import music_labels_controller
from flask_database.app.lab4_db.auth.domain.orders.music_labels import MusicLabels

music_labels_bp = Blueprint('music_labels', __name__, url_prefix='/music_labels')


@music_labels_bp.get('')
def get_all_music_labels() -> Response:
    return make_response(jsonify(music_labels_controller.find_all()), HTTPStatus.OK)


@music_labels_bp.post('')
def create_music_labels() -> Response:
    content = request.get_json()
    music_labels = MusicLabels.create_from_dto(content)
    music_labels_controller.create(music_labels)
    return make_response(jsonify(music_labels.put_into_dto()), HTTPStatus.CREATED)


@music_labels_bp.get('/<int:music_labels_id>')
def get_music_labels(music_labels_id: int) -> Response:

    return make_response(jsonify(music_labels_controller.find_by_id(music_labels_id)), HTTPStatus.OK)


@music_labels_bp.put('/<int:music_labels_id>')
def update_music_labels(music_labels_id: int) -> Response:
    content = request.get_json()
    music_labels = MusicLabels.create_from_dto(content)
    music_labels_controller.update(music_labels_id, music_labels)
    return make_response("Music_labels updated", HTTPStatus.OK)


@music_labels_bp.patch('/<int:music_labels_id>')
def patch_music_labels(music_labels_id: int) -> Response:
    content = request.get_json()
    music_labels_controller.patch(music_labels_id, content)
    return make_response("Music_labels updated", HTTPStatus.OK)


@music_labels_bp.delete('/<int:music_labels_id>')
def delete_music_labels(music_labels_id: int) -> Response:
    music_labels_controller.delete(music_labels_id)
    return make_response("Music_labels deleted", HTTPStatus.OK)
