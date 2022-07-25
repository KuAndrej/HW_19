from dao.model.user import User


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class UserDAO:
    """Объект доступа к данным для user модели."""
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """Метод для получения одного пользователя по его ID."""
        return self.session.query(User).get(bid)

    def get_all(self):
        """Метод для получения всех пользователей."""
        return self.session.query(User).all()

    def get_user_by_username(self, username: str):
        """Метод для получения пользователей с определенным именем по запросу типа /users/?username=10."""
        return self.session.query(User).filter(User.username == username).first()

    def get_by_role_user(self, role="user"):
        """Метод для получения пользователей с ролью user."""
        user_role = self.session.query(User).filter(User.role == role).all()
        for roles in user_role:
            if roles == "user":
                return roles
            return "Not Found", 404

    def get_by_role_admin(self, role="admin"):
        """Метод для получения пользователей с ролью admin."""
        admin_role = self.session.query(User).filter(User.role == role).all()
        for roles in admin_role:
            if roles == "admin":
                return roles
            return "Not Found", 404

    def create_user(self, user):
        """Метод для создания нового пользователя."""
        user_ent = User(**user)
        self.session.add(user_ent)
        self.session.commit()
        return user_ent

    def delete(self, bid):
        """Метод для удаления пользователя."""
        user = self.get_one(bid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        """Метод для обновления пользователя."""
        user = self.get_one(user_d.get("id"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role_id = user_d.get("role_id")

        self.session.add(user)
        self.session.commit()
