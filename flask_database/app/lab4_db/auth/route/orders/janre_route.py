from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import janre_controller
from flask_database.app.lab4_db.auth.domain.orders.janre import Janre

janre_bp = Blueprint('janre', __name__, url_prefix='/janre')


@janre_bp.get('')
def get_all_janre() -> Response:
    return make_response(jsonify(janre_controller.find_all()), HTTPStatus.OK)


@janre_bp.post('')
def create_janre() -> Response:
    content = request.get_json()
    janre = Janre.create_from_dto(content)
    janre_controller.create(janre)
    return make_response(jsonify(janre.put_into_dto()), HTTPStatus.CREATED)


@janre_bp.get('/<int:janre_id>')
def get_janre(janre_id: int) -> Response:
    return make_response(jsonify(janre_controller.find_by_id(janre_id)), HTTPStatus.OK)


@janre_bp.put('/<int:janre_id>')
def update_janre(janre_id: int) -> Response:
    content = request.get_json()
    janre = Janre.create_from_dto(content)
    janre_controller.update(janre_id, janre)
    return make_response("Janre updated", HTTPStatus.OK)


@janre_bp.patch('/<int:janre_id>')
def patch_janre(janre_id: int) -> Response:
    content = request.get_json()
    janre_controller.patch(janre_id, content)
    return make_response("Janre updated", HTTPStatus.OK)


@janre_bp.delete('/<int:janre_id>')
def delete_janre(janre_id: int) -> Response:
    janre_controller.delete(janre_id)
    return make_response("Janre deleted", HTTPStatus.OK)


@janre_bp.post('/create-db-name-janre')
def create_dbs():
    janre_controller.create_db_name_janre()
    return make_response("Databases was created", HTTPStatus.OK)
