from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from helpers.decorators import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')

"""Представления для сущности режиссеров /directors/."""
@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """Метод для получения всех режиссеров."""
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @auth_required
    @admin_required
    def post(self):
        """Метод для добавления нового режиссера."""
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{director.id}"}


"""Представления для сущности режиссеров /directors/<int:rid>."""
@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        """Метод для получения одного режиссера по его ID."""
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @auth_required
    @admin_required
    def put(self, rid):
        """Метод для изменения одного режиссера."""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = rid
        director_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, rid):
        """Метод для удаления одного режиссера."""
        director_service.delete(rid)
        return "", 204
