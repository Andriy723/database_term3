from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import person_profile_controller
from flask_database.app.lab4_db.auth.domain.orders.person_profile import PersonProfile

person_profile_bp = Blueprint('person_profile', __name__, url_prefix='/person_profile')


@person_profile_bp.get('')
def get_all_person_profile() -> Response:
    return make_response(jsonify(person_profile_controller.find_all()), HTTPStatus.OK)


@person_profile_bp.post('')
def create_person_profile() -> Response:
    content = request.get_json()
    person_profile = PersonProfile.create_from_dto(content)
    person_profile_controller.create(person_profile)
    return make_response(jsonify(person_profile.put_into_dto()), HTTPStatus.CREATED)


@person_profile_bp.get('/<int:person_profile_id>')
def get_person_profile(person_profile_id: int) -> Response:
    return make_response(jsonify(person_profile_controller.find_by_id(person_profile_id)), HTTPStatus.OK)


@person_profile_bp.put('/<int:person_profile_id>')
def update_person_profile(person_profile_id: int) -> Response:
    content = request.get_json()
    person_profile = PersonProfile.create_from_dto(content)
    person_profile_controller.update(person_profile_id, person_profile)
    return make_response("Person_profile updated", HTTPStatus.OK)


@person_profile_bp.patch('/<int:person_profile_id>')
def patch_person_profile(person_profile_id: int) -> Response:
    content = request.get_json()
    person_profile_controller.patch(person_profile_id, content)
    return make_response("Person_profile updated", HTTPStatus.OK)


@person_profile_bp.delete('/<int:person_profile_id>')
def delete_person_profile(person_profile_id: int) -> Response:
    person_profile_controller.delete(person_profile_id)
    return make_response("Person_profile deleted", HTTPStatus.OK)
