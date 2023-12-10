from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import country_controller
from flask_database.app.lab4_db.auth.domain.orders.country import Country

country_bp = Blueprint('country', __name__, url_prefix='/country')


@country_bp.get('')
def get_all_country() -> Response:
    return make_response(jsonify(country_controller.find_all()), HTTPStatus.OK)


@country_bp.post('')
def create_country() -> Response:
    content = request.get_json()
    country = Country.create_from_dto(content)
    country_controller.create(country)
    return make_response(jsonify(country.put_into_dto()), HTTPStatus.CREATED)


@country_bp.get('/<int:country_id>')
def get_country(country_id: int) -> Response:
    return make_response(jsonify(country_controller.find_by_id(country_id)), HTTPStatus.OK)


@country_bp.put('/<int:country_id>')
def update_country(country_id: int) -> Response:
    content = request.get_json()
    country = Country.create_from_dto(content)
    country_controller.update(country_id, country)
    return make_response("Country updated", HTTPStatus.OK)


@country_bp.patch('/<int:country_id>')
def patch_country(country_id: int) -> Response:
    content = request.get_json()
    country_controller.patch(country_id, content)
    return make_response("Country updated", HTTPStatus.OK)


@country_bp.delete('/<int:country_id>')
def delete_country(country_id: int) -> Response:
    country_controller.delete(country_id)
    return make_response("Country deleted", HTTPStatus.OK)


@country_bp.post('/insert-into-country/<string:city>/<string:current_place>')
def insert_into_country(city, current_place):
    country_controller.insert_into_country_parameters(city, current_place)
    return make_response("Country created", HTTPStatus.OK)


@country_bp.post('/insert-strings-country/<string:city>/<string:current_place>')
def insert_strings_country(city, current_place):
    country_controller.insert_strings_country_parameters(city, current_place)
    return make_response("Strings countries created", HTTPStatus.OK)
