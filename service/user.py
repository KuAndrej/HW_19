import base64
import hashlib
import hmac
from helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    """Класс с бизнес-логикой сущности пользователи."""
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        """Метод для получения одного пользователя по его ID."""
        return self.dao.get_one(bid)

    def get_all(self):
        """Метод для получения всех пользователей по запросу типа /users/.
        Для получения пользователей с определенным именем по запросу типа /users/?username=Олег.
        Для получения пользователей с определенной ролью по запросу типа /users/?role=user."""
        return self.dao.get_all()

    def get_user_by_username(self, username):
        """Метод для получения пользователей с определенным именем по запросу типа /users/?username=10."""
        return self.dao.get_user_by_username(username)

    def get_by_role_user(self, value):
        """Метод для получения пользователей с ролью user."""
        return self.dao.get_by_role_user(value)

    def get_by_role_admin(self, value):
        """Метод для получения пользователей с ролью admin."""
        return self.dao.get_by_role_admin(value)

    def get_hash(self, password):
        """Метод для генерации хеша пароля пользователя."""
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password):
        """Метод для сравнения паролей."""
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),  # Преобразовываем пароль в байты
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            ))

    def create_user(self, user):
        """Метод для создания нового пользователя."""
        user['password'] = self.get_hash(user['password'])
        return self.dao.create_user(user)

    def update(self, user_d):
        """Метод для обновления одного пользователя."""
        user_d["password"] = self.get_hash(user_d.get("password"))
        self.dao.update(user_d)
        return self.dao

    def delete(self, bid):
        """Метод для удаления одного пользователя."""
        self.dao.delete(bid)
