from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import follower_has_creator_controller
from flask_database.app.lab4_db.auth.domain.orders.follower_has_creator import FollowerHasCreator

follower_has_creator_bp = Blueprint('follower_has_creator', __name__, url_prefix='/follower_has_creator')


@follower_has_creator_bp.get('')
def get_all_follower_has_creator() -> Response:
    return make_response(jsonify(follower_has_creator_controller.find_all()), HTTPStatus.OK)


@follower_has_creator_bp.post('')
def create_follower_has_creator() -> Response:
    content = request.get_json()
    follower_has_creator = FollowerHasCreator.create_from_dto(content)
    follower_has_creator_controller.create(follower_has_creator)
    return make_response(jsonify(follower_has_creator.put_into_dto()), HTTPStatus.CREATED)


@follower_has_creator_bp.get('/<int:follower_has_creator_id>')
def get_follower_has_creatorr(follower_has_creator_id: int) -> Response:
    return make_response(jsonify(follower_has_creator_controller.find_by_id(follower_has_creator_id)), HTTPStatus.OK)


@follower_has_creator_bp.put('/<int:follower_has_creator_id>')
def update_follower_has_creator(follower_has_creator_id: int) -> Response:
    content = request.get_json()
    follower_has_creator = FollowerHasCreator.create_from_dto(content)
    follower_has_creator_controller.update(follower_has_creator_id, follower_has_creator)
    return make_response("Follower_has_creator updated", HTTPStatus.OK)


@follower_has_creator_bp.patch('/<int:follower_has_creator_id>')
def patch_follower_has_creator(follower_has_creator_id: int) -> Response:
    content = request.get_json()
    follower_has_creator_controller.patch(follower_has_creator_id, content)
    return make_response("Follower_has_creator updated", HTTPStatus.OK)


@follower_has_creator_bp.delete('/<int:follower_has_creator_id>')
def delete_follower_has_creator(follower_has_creator_id: int) -> Response:
    follower_has_creator_controller.delete(follower_has_creator_id)
    return make_response("Follower_has_creator deleted", HTTPStatus.OK)
