from flask import request
from flask_restx import Resource, Namespace
from dao.model.movie import MovieSchema
from helpers.decorators import auth_required, admin_required
from implemented import movie_service

movie_ns = Namespace('movies')

"""Представления для сущности фильмы /movies/."""
@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """Метод для получения всех фильмов.
        Для получения фильма/ов с одним режиссером.
        Для получения фильма/ов с одним жанром.
        Для получения фильма/ов за определенный год."""
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    @auth_required
    @admin_required
    def post(self):
        """Метод для добавления нового фильма."""
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


"""Представления для сущности фильмы /movies/<int:bid>."""
@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        """Метод для получения одного фильма по его ID."""
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @auth_required
    @admin_required
    def put(self, bid):
        """Метод для изменения одного фильма по его ID."""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @auth_required
    @admin_required
    def delete(self, bid):
        """Метод для удаления одного фильма по его ID."""
        movie_service.delete(bid)
        return "", 204
