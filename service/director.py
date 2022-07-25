from dao.director import DirectorDAO


class DirectorService:
    """Класс с бизнес-логикой сущности режиссеры."""
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        """Метод для получения одного режиссера по ID."""
        return self.dao.get_one(bid)

    def get_all(self):
        """Метод для получения всех режиссеров."""
        return self.dao.get_all()

    def create(self, director_d):
        """Метод для создания нового режиссера."""
        return self.dao.create(director_d)

    def update(self, director_d):
        """Метод для обновления одного режиссера."""
        self.dao.update(director_d)
        return self.dao

    def delete(self, rid):
        """Метод для удаления одного режиссера."""
        self.dao.delete(rid)
