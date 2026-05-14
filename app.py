from flask import Flask, render_template, request, redirect # Add 'render_template' to your listed imports from Flask

from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.film_repository import FilmRepository
from lib.user_repository import UserRepository
from lib.book import Book
from lib.films import Film
from lib.user import User

# instantiate a Flask app object
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/books', methods=['GET'])
def get_all_books(): 
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)


@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/quotes', methods=['GET'])
def get_quotes():
    quote = ["inspo1"]
    return render_template("quotes.html", quote=quote)

@app.route('/authors', methods=['GET'])
def list_authors():
    return [
    {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
    },
    {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
    },
    {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
    },
    {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
    }
    ]

@app.route('/films', methods=['GET'])
def get_all_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    return render_template("films.html", films=films)

@app.route('/films', methods=['POST'])
def add_new_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film_details = request.form
    film = Film(title=film_details["title"], genre=film_details["genre"], release_year=film_details["release_year"])
    film_repository.create(film)
    return redirect("/films")

@app.route('/users/new', methods = ['GET'])
def get_signup_form():
    return render_template("signup_form.html")


@app.route('/users', methods = ['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/books")

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
