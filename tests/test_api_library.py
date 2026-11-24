import pytest
from src.api.app import app, reset_data


@pytest.fixture
def client():
    app.config["TESTING"] = True
    reset_data()
    with app.test_client() as c:
        yield c


def test_add_and_get_book(client):
    res = client.post(
        "/books",
        json={
            "title": "Clean Code",
            "isbn": "9780132350884",
            "author": "Robert C. Martin",
            "total_copies": 2,
        },
    )
    assert res.status_code == 201
    assert set(res.get_json().keys()) == {"title", "isbn", "author", "available_copies"}
    assert res.get_json()["available_copies"] == 2

    get_res = client.get("/books/9780132350884")
    assert get_res.status_code == 200
    assert get_res.get_json()["title"] == "Clean Code"


def test_borrow_and_return_book(client):
    client.post(
        "/books",
        json={"title": "Book A", "isbn": "9780132350884", "author": "Author A", "total_copies": 1},
    )
    b_res = client.post("/members/M1/borrow", json={"isbn": "9780132350884"})
    assert b_res.status_code == 200
    assert b_res.get_json()["available_copies"] == 0

    r_res = client.post("/members/M1/return", json={"isbn": "9780132350884"})
    assert r_res.status_code == 200
    assert r_res.get_json()["available_copies"] == 1


def test_fines_endpoint(client):
    res = client.get("/members/M1/fines?days_overdue=5")
    assert res.status_code == 200
    assert res.get_json()["tier"] == "Low"


def test_unknown_book_404_and_missing_title_400(client):
    not_found = client.get("/books/9780000000000")
    assert not_found.status_code == 404

    bad_req = client.post(
        "/books",
        json={"isbn": "9780132350884", "author": "Author A", "total_copies": 1},
    )
    assert bad_req.status_code == 400
    assert "title" in bad_req.get_json()["error"].lower()


def test_zero_copies_and_sixth_book_limit_400(client):
    client.post(
        "/books",
        json={"title": "Solo Book", "isbn": "9781111111111", "author": "Auth", "total_copies": 1},
    )
    client.post("/members/M1/borrow", json={"isbn": "9781111111111"})
    zero_res = client.post("/members/M2/borrow", json={"isbn": "9781111111111"})
    assert zero_res.status_code == 400

    for i in range(6):
        isbn = f"978222222222{i}"
        client.post(
            "/books",
            json={"title": f"B{i}", "isbn": isbn, "author": "Auth", "total_copies": 1},
        )
        r = client.post("/members/M3/borrow", json={"isbn": isbn})
        assert r.status_code == (200 if i < 5 else 400)


def test_books_list_schema(client):
    client.post(
        "/books",
        json={"title": "Schema Book", "isbn": "9783333333333", "author": "Auth", "total_copies": 1},
    )
    res = client.get("/books")
    assert res.status_code == 200
    items = res.get_json()
    assert isinstance(items, list)
    assert set(items[0].keys()) == {"title", "isbn", "author", "available_copies"}