from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import downloading_song_has_person_profile_controller
from flask_database.app.lab4_db.auth.domain.orders.downloading_song_has_person_profile import DownloadingSongHasPersonProfile

downloading_song_has_person_profile_bp = Blueprint('downloading_song_has_person_profile', __name__,
                                                   url_prefix='/downloading_song_has_person_profile')


@downloading_song_has_person_profile_bp.get('')
def get_all_downloading_song_has_person_profile() -> Response:
    return make_response(jsonify(downloading_song_has_person_profile_controller.find_all()), HTTPStatus.OK)


@downloading_song_has_person_profile_bp.post('')
def create_downloading_song_has_person_profile() -> Response:
    content = request.get_json()
    downloading_song_has_person_profile = DownloadingSongHasPersonProfile.create_from_dto(content)
    downloading_song_has_person_profile_controller.create(downloading_song_has_person_profile)
    return make_response(jsonify(downloading_song_has_person_profile.put_into_dto()), HTTPStatus.CREATED)


@downloading_song_has_person_profile_bp.get('/<int:downloading_song_has_person_profile_id>')
def get_downloading_song_has_person_profile(downloading_song_has_person_profile_id: int) -> Response:
    return make_response(jsonify(downloading_song_has_person_profile_controller.
                                 find_by_id(downloading_song_has_person_profile_id)), HTTPStatus.OK)


@downloading_song_has_person_profile_bp.put('/<int:downloading_song_has_person_profile_id>')
def update_downloading_song_has_person_profile(downloading_song_has_person_profile_id: int) -> Response:
    content = request.get_json()
    downloading_song_has_person_profile = DownloadingSongHasPersonProfile.create_from_dto(content)
    downloading_song_has_person_profile_controller.update(downloading_song_has_person_profile_id,
                                                          downloading_song_has_person_profile)
    return make_response("Downloading_song_has_person_profile updated", HTTPStatus.OK)


@downloading_song_has_person_profile_bp.patch('/<int:downloading_song_has_person_profile_id>')
def patch_downloading_song_has_person_profile(downloading_song_has_person_profile_id: int) -> Response:
    content = request.get_json()
    downloading_song_has_person_profile_controller.patch(downloading_song_has_person_profile_id, content)
    return make_response("Downloading_song_has_person_profile updated", HTTPStatus.OK)


@downloading_song_has_person_profile_bp.delete('/<int:downloading_song_has_person_profile_id>')
def delete_downloading_song_has_person_profile(downloading_song_has_person_profile_id: int) -> Response:
    downloading_song_has_person_profile_controller.delete(downloading_song_has_person_profile_id)
    return make_response("Downloading_song_has_person_profile deleted", HTTPStatus.OK)
