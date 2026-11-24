import threading
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from werkzeug.serving import make_server
from pages.catalog_page import CatalogPage
from src.api.app import app, reset_data


@pytest.fixture
def live_server():
    reset_data()
    server = make_server("127.0.0.1", 0, app)
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    time.sleep(0.2)
    yield f"http://127.0.0.1:{port}"
    server.shutdown()


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


def test_four_catalog_journeys(driver, live_server):
    page = CatalogPage(driver)
    page.open(live_server)

    # 1. Add a book and confirm it appears in the table
    page.add_book("Clean Code", "9780132350884", "Robert C. Martin", 1)
    assert "9780132350884" in page.book_row_text("9780132350884")
    assert page.get_available_copies_display("9780132350884") == 1

    # 2. Borrow the last copy and confirm available copies decrease to 0
    page.click_borrow("9780132350884")
    page.wait.until(lambda d: page.get_available_copies_display("9780132350884") == 0)
    assert page.get_available_copies_display("9780132350884") == 0

    # 3. Attempt to borrow again when no copies remain
    page.click_borrow("9780132350884")
    assert "no copies available" in page.status_message().lower()

    # 4. Empty title validation message without calling API
    page.add_book("", "9789999999999", "Some Author", 1)
    assert "title is required" in page.status_message().lower()