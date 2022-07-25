from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from helpers.decorators import admin_required, auth_required
from implemented import user_service

user_ns = Namespace('users')

"""Представления для сущности пользователи /users/."""
@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        """Метод для получения всех пользователей по запросу типа /users/.
        Для получения пользователей с определенным именем по запросу типа /users/?username=Олег.
        Для получения пользователей с определенной ролью по запросу типа /users/?role=user."""
        username = request.args.get("username")
        admin = request.args.get("admin")
        user = request.args.get("user")

        if username:
            user_name = user_service.get_user_by_username(username)
            return UserSchema(many=True).dump(user_name), 200

        if admin:
            admin_u = user_service.get_by_role_admin(admin)
            return UserSchema(many=True).dump(admin_u), 200

        if user:
            user_u = user_service.get_by_role_user(user)
            return UserSchema(many=True).dump(user_u), 200

        all_users = user_service.get_all()
        res = UserSchema(many=True).dump(all_users)
        return res, 200

    def post(self):
        """Метод для создания пользователя."""
        req_json = request.json
        user_service.create_user(req_json)
        return "", 201


"""Представления для сущности пользователи /users/<int:bid>."""
@user_ns.route('/<int:bid>')
class UserView(Resource):
    def get(self, bid):
        """Метод для получения одного пользователя по его ID."""
        try:
            user = user_service.get_one(bid)
            result = UserSchema().dump(user)
            return result, 200
        except Exception as ex:
            return ex, 404

    @auth_required
    @admin_required
    def put(self, bid):
        """Метод для изменения одного пользователя по его ID."""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        user_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, bid):
        """Метод для удаления одного пользователя по его ID."""
        user_service.delete(bid)
        return "", 204
