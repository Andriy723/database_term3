from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import janre_has_music_controller
from flask_database.app.lab4_db.auth.domain.orders.janre_has_music import JanreHasMusic

janre_has_music_bp = Blueprint('janre_has_music', __name__, url_prefix='/janre_has_music')


@janre_has_music_bp.get('')
def get_all_janre_has_music() -> Response:
    return make_response(jsonify(janre_has_music_controller.find_all()), HTTPStatus.OK)


@janre_has_music_bp.post('')
def create_janre_has_music() -> Response:
    content = request.get_json()
    janre_has_music = JanreHasMusic.create_from_dto(content)
    janre_has_music_controller.create(janre_has_music)
    return make_response(jsonify(janre_has_music.put_into_dto()), HTTPStatus.CREATED)


@janre_has_music_bp.get('/<int:janre_has_music_id>')
def get_janre_has_music(janre_has_music_id: int) -> Response:
    return make_response(jsonify(janre_has_music_controller.find_by_id(janre_has_music_id)), HTTPStatus.OK)


@janre_has_music_bp.put('/<int:janre_has_music_id>')
def update_janre_has_music(janre_has_music_id: int) -> Response:
    content = request.get_json()
    janre_has_music = JanreHasMusic.create_from_dto(content)
    janre_has_music_controller.update(janre_has_music_id, janre_has_music)
    return make_response("Janre_has_music updated", HTTPStatus.OK)


@janre_has_music_bp.patch('/<int:janre_has_music_id>')
def patch_janre_has_music(janre_has_music_id: int) -> Response:
    content = request.get_json()
    janre_has_music_controller.patch(janre_has_music_id, content)
    return make_response("Janre_has_music updated", HTTPStatus.OK)


@janre_has_music_bp.delete('/<int:janre_has_music_id>')
def delete_janre_has_music(janre_has_music_id: int) -> Response:
    janre_has_music_controller.delete(janre_has_music_id)
    return make_response("Janre_has_music deleted", HTTPStatus.OK)
