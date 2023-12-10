from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import follower_controller
from flask_database.app.lab4_db.auth.domain.orders.follower import Follower

follower_bp = Blueprint('follower', __name__, url_prefix='/follower')


@follower_bp.get('')
def get_all_follower() -> Response:
    return make_response(jsonify(follower_controller.find_all()), HTTPStatus.OK)


@follower_bp.post('')
def create_follower() -> Response:
    content = request.get_json()
    follower = Follower.create_from_dto(content)
    follower_controller.create(follower)
    return make_response(jsonify(follower.put_into_dto()), HTTPStatus.CREATED)


@follower_bp.get('/<int:follower_id>')
def get_follower(follower_id: int) -> Response:
    return make_response(jsonify(follower_controller.find_by_id(follower_id)), HTTPStatus.OK)


@follower_bp.put('/<int:follower_id>')
def update_follower(follower_id: int) -> Response:
    content = request.get_json()
    follower = Follower.create_from_dto(content)
    follower_controller.update(follower_id, follower)
    return make_response("Follower updated", HTTPStatus.OK)


@follower_bp.patch('/<int:follower_id>')
def patch_follower(follower_id: int) -> Response:
    content = request.get_json()
    follower_controller.patch(follower_id, content)
    return make_response("Follower updated", HTTPStatus.OK)


@follower_bp.delete('/<int:follower_id>')
def delete_follower(follower_id: int) -> Response:
    follower_controller.delete(follower_id)
    return make_response("Follower deleted", HTTPStatus.OK)
