from dao.model.director import Director


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class DirectorDAO:
    """Объект доступа к данным для director модели."""
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """Метод для получения одного режиссера по ID."""
        return self.session.query(Director).get(bid)

    def get_all(self):
        """Метод для получения всех режиссеров."""
        return self.session.query(Director).all()

    def create(self, director_d):
        """Метод для создания одного режиссера."""
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """Метод для удаления одного режиссера."""
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        """Метод для обновления одного режиссера."""
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
