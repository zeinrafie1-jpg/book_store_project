from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_has_title(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Welcome to AceReads")

def test_books_has_title(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    h1 = page.locator("h1")
    expect(h1).to_have_text("My Books")

def test_books_are_listed(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    books = page.locator("h3")
    expected_books = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott'
    ]
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

def test_create_new_book(page:Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("1984")
    page.get_by_placeholder("Author").fill("George Orwell")
    page.get_by_role("button", name="Submit").click()
    books = page.locator("h3")
    new_book = books.all_inner_texts()[-1]
    assert new_book == "1984 by George Orwell"

def test_create_new_film(page:Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films_test.sql")
    page.goto("http://127.0.0.1:5001/films")
    page.get_by_placeholder("Title").fill("Seven")
    page.get_by_placeholder("Genre").fill("Crime-horror")
    page.get_by_placeholder("Release Year").fill("1995")
    page.get_by_role("button", name="Submit").click()
    films = page.locator("li")
    new_films = films.all_inner_texts()[-1]
    assert new_films == "Seven / Crime-horror / 1995"
    