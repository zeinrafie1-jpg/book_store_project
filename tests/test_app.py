import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# a descriptive test name
def test_get_books_returns_a_200():
    # here's where we make the test client
    client = app.test_client()

    # here's where we make the request
    response = client.get("/books")

    # here's where we assert that the response's status code is 200
    assert response.status_code == 200

# a descriptive test name
def test_get_books_returns_all_the_books():
    client = app.test_client()
    response = client.get("/books")
    assert b"The Gruffalo by Julia Donaldson" in response.data
    assert b"Ada Twist, Scientist by Andrea Beaty" in response.data
    
# a descriptive test name
def test_get_authors_returns_a_200():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200

def test_get_authors_returns_all_the_authors():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
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

def test_get_quotes_returns_a_200():
    client = app.test_client()
    response = client.get("/quotes")
    assert response.status_code == 200

def test_films_returns_200():
    client = app.test_client()
    response = client.get("/films")
    assert response.status_code == 200

def test_films_returns_list_page():
    client = app.test_client()
    response = client.get("/films")
    assert "Film1" in response.data.decode('utf-8')
    assert "Grown Ups" in response.data.decode('utf-8') 


    #     'Film1', 'Horror', 2000),
    #     Film(2, 'Grown Ups', 'Comedy', 2010),
    #     Film(3, 'The Devil Wears Prada 2', 'Comedy', 2026)
    # ]
    # assert films == expected_films
