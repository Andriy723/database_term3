from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import country_has_music_controller
from flask_database.app.lab4_db.auth.domain.orders.country_has_music import CountryHasMusic

country_has_music_bp = Blueprint('country_has_music', __name__, url_prefix='/country_has_music')


@country_has_music_bp.get('')
def get_all_country_has_music() -> Response:
    return make_response(jsonify(country_has_music_controller.find_all()), HTTPStatus.OK)


@country_has_music_bp.post('')
def create_country_has_music() -> Response:
    content = request.get_json()
    country_has_music = CountryHasMusic.create_from_dto(content)
    country_has_music_controller.create(country_has_music)
    return make_response(jsonify(country_has_music.put_into_dto()), HTTPStatus.CREATED)


@country_has_music_bp.get('/<int:country_has_music_id>')
def get_country(country_has_music_id: int) -> Response:
    return make_response(jsonify(country_has_music_controller.find_by_id(country_has_music_id)), HTTPStatus.OK)


@country_has_music_bp.put('/<int:country_has_music_id>')
def update_country(country_has_music_id: int) -> Response:
    content = request.get_json()
    country_has_music = CountryHasMusic.create_from_dto(content)
    country_has_music_controller.update(country_has_music_id, country_has_music)
    return make_response("Country_has_music updated", HTTPStatus.OK)


@country_has_music_bp.patch('/<int:country_has_music_id>')
def patch_country(country_has_music_id: int) -> Response:
    content = request.get_json()
    country_has_music_controller.patch(country_has_music_id, content)
    return make_response("Country_has_music updated", HTTPStatus.OK)


@country_has_music_bp.delete('/<int:country_has_music_id>')
def delete_albom(country_has_music_id: int) -> Response:
    country_has_music_controller.delete(country_has_music_id)
    return make_response("Country_has_music deleted", HTTPStatus.OK)


@country_has_music_bp.post('/insert-country-has-music/<string:id_country>/<string:id_music>')
def insert_country_has_music(id_country, id_music):
    country_has_music_controller.insert_into_country_has_music(id_country, id_music)
    if id_country == id_music:
        return make_response("Country has music created", HTTPStatus.OK)
    else:
        return make_response("Something is wrong", HTTPStatus.BAD_REQUEST)
