from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import albom_controller
from flask_database.app.lab4_db.auth.domain.orders.albom import Albom

albom_bp = Blueprint('albom', __name__, url_prefix='/albom')


@albom_bp.get('')
def get_all_albom() -> Response:
    return make_response(jsonify(albom_controller.find_all()), HTTPStatus.OK)


@albom_bp.post('')
def create_albom() -> Response:
    content = request.get_json()
    albom = Albom.create_from_dto(content)
    albom_controller.create(albom)
    return make_response(jsonify(albom.put_into_dto()), HTTPStatus.CREATED)


@albom_bp.get('/<int:albom_id>')
def get_albom(albom_id: int) -> Response:
    return make_response(jsonify(albom_controller.find_by_id(albom_id)), HTTPStatus.OK)


@albom_bp.put('/<int:albom_id>')
def update_albom(albom_id: int) -> Response:
    content = request.get_json()
    albom = Albom.create_from_dto(content)
    albom_controller.update(albom_id, albom)
    return make_response("Albom updated", HTTPStatus.OK)


@albom_bp.patch('/<int:albom_id>')
def patch_albom(albom_id: int) -> Response:
    content = request.get_json()
    albom_controller.patch(albom_id, content)
    return make_response("Albom updated", HTTPStatus.OK)


@albom_bp.delete('/<int:albom_id>')
def delete_albom(albom_id: int) -> Response:
    albom_controller.delete(albom_id)
    return make_response("Albom deleted", HTTPStatus.OK)
