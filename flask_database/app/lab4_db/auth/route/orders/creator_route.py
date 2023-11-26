from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import creator_controller
from flask_database.app.lab4_db.auth.domain.orders.creator import Creator

creator_bp = Blueprint('creator', __name__, url_prefix='/creator')


@creator_bp.get('')
def get_all_creator() -> Response:
    return make_response(jsonify(creator_controller.find_all()), HTTPStatus.OK)


@creator_bp.post('')
def create_creator() -> Response:
    content = request.get_json()
    creator = Creator.create_from_dto(content)
    creator_controller.create(creator)
    return make_response(jsonify(creator.put_into_dto()), HTTPStatus.CREATED)


@creator_bp.get('/<int:creator_id>')
def get_creator(creator_id: int) -> Response:
    return make_response(jsonify(creator_controller.find_by_id(creator_id)), HTTPStatus.OK)


@creator_bp.put('/<int:creator_id>')
def update_creator(creator_id: int) -> Response:
    content = request.get_json()
    creator = Creator.create_from_dto(content)
    creator_controller.update(creator_id, creator)
    return make_response("Creator updated", HTTPStatus.OK)


@creator_bp.patch('/<int:creator_id>')
def patch_creator(creator_id: int) -> Response:
    content = request.get_json()
    creator_controller.patch(creator_id, content)
    return make_response("Creator updated", HTTPStatus.OK)


@creator_bp.delete('/<int:creator_id>')
def delete_creator(creator_id: int) -> Response:
    creator_controller.delete(creator_id)
    return make_response("Creator deleted", HTTPStatus.OK)
