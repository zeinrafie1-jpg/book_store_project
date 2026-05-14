from lib.films import Film

class FilmRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from films')
        films = []
        for row in rows:
            item = Film(row["title"], row["genre"], row["release_year"], row["id"])
            films.append(item)
        return films
    
    def create(self, film):
        self._connection.execute(
            'INSERT INTO films (title, genre, release_year) values (%s, %s, %s)', 
            [film.title, film.genre, film.release_year]
        )
        return None