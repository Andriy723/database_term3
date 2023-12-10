from http import HTTPStatus
from flask import jsonify
from flask_database.app.lab4_db.auth.controller.general_controller import GeneralController
from flask_database.app.lab4_db.auth.service import music_service


class MusicController(GeneralController):

    _service = music_service

    def get_operations(self, operation):
        return jsonify(self._service.get_operations(operation)), HTTPStatus.OK

    def call_function_for_operations(self, operation):
        self._service.call_function_for_operations(operation)
