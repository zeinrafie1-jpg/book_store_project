from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def create(self, user):
        self._connection.execute(
            'INSERT INTO users (username, password) values (%s, %s)',
            [user.username, user.password]
        )
        return None