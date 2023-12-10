from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import music_controller
from flask_database.app.lab4_db.auth.domain.orders.music import Music

music_bp = Blueprint('music', __name__, url_prefix='/music')


@music_bp.get('')
def get_all_music() -> Response:
    return make_response(jsonify(music_controller.find_all()), HTTPStatus.OK)


@music_bp.post('')
def create_music() -> Response:
    content = request.get_json()
    music = Music.create_from_dto(content)
    music_controller.create(music)
    return make_response(jsonify(music.put_into_dto()), HTTPStatus.CREATED)


@music_bp.get('/<int:music_id>')
def get_music(music_id: int) -> Response:
    return make_response(jsonify(music_controller.find_by_id(music_id)), HTTPStatus.OK)


@music_bp.put('/<int:music_id>')
def update_music(music_id: int) -> Response:
    content = request.get_json()
    music = Music.create_from_dto(content)
    music_controller.update(music_id, music)
    return make_response("Music updated", HTTPStatus.OK)


@music_bp.patch('/<int:music_id>')
def patch_music(music_id: int) -> Response:
    content = request.get_json()
    music_controller.patch(music_id, content)
    return make_response("Music updated", HTTPStatus.OK)


@music_bp.delete('/<int:music_id>')
def delete_music(music_id: int) -> Response:
    music_controller.delete(music_id)
    return make_response("Music deleted", HTTPStatus.OK)


@music_bp.route('/get-operations/<string:function>')
def get_operations_route(function) -> Response:
    operation = function.upper()

    if operation in ['MAX', 'MIN', 'SUM', 'AVG']:
        return music_controller.get_operations(operation)
    else:
        return make_response("Invalid operation", HTTPStatus.BAD_REQUEST)
