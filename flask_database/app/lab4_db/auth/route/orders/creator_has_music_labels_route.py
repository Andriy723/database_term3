from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_database.app.lab4_db.auth.controller import creator_has_music_labels_controller
from flask_database.app.lab4_db.auth.domain.orders.creator_has_music_labels import CreatorHasMusicLabels

creator_has_music_labels_bp = Blueprint('creator_has_music_labels', __name__, url_prefix='/creator_has_music_labels')


@creator_has_music_labels_bp.get('')
def get_all_creator_has_music_labels() -> Response:
    return make_response(jsonify(creator_has_music_labels_controller.find_all()), HTTPStatus.OK)


@creator_has_music_labels_bp.post('')
def create_creator_has_music_labels() -> Response:
    content = request.get_json()
    creator_has_music_labels = CreatorHasMusicLabels.create_from_dto(content)
    creator_has_music_labels_controller.create(creator_has_music_labels)
    return make_response(jsonify(creator_has_music_labels.put_into_dto()), HTTPStatus.CREATED)


@creator_has_music_labels_bp.get('/<int:creator_has_music_labels_id>')
def get_creator_has_music_labels(creator_has_music_labels_id: int) -> Response:
    return make_response(jsonify(creator_has_music_labels_controller.
                                 find_by_id(creator_has_music_labels_id)), HTTPStatus.OK)


@creator_has_music_labels_bp.put('/<int:creator_has_music_labels_id>')
def update_creator_has_music_labels(creator_has_music_labels_id: int) -> Response:
    content = request.get_json()
    creator_has_music_labels = CreatorHasMusicLabels.create_from_dto(content)
    creator_has_music_labels_controller.update(creator_has_music_labels_id, creator_has_music_labels)
    return make_response("Creator_has_music_labels updated", HTTPStatus.OK)


@creator_has_music_labels_bp.patch('/<int:creator_has_music_labels_id>')
def patch_creator_has_music_labels(creator_has_music_labels_id: int) -> Response:
    content = request.get_json()
    creator_has_music_labels_controller.patch(creator_has_music_labels_id, content)
    return make_response("Creator_has_music_labels updated", HTTPStatus.OK)


@creator_has_music_labels_bp.delete('/<int:creator_has_music_labels_id>')
def delete_creator_has_music_labels(creator_has_music_labels_id: int) -> Response:
    creator_has_music_labels_controller.delete(creator_has_music_labels_id)
    return make_response("Creator_has_music_labels_has_music_labels deleted", HTTPStatus.OK)
