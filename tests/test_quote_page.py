from playwright.sync_api import Page, expect

def test_books_has_title(page: Page):
    page.goto("http://127.0.0.1:5001/quotes")
    p = page.locator("p")
    expect(p).to_have_text("inspo1")