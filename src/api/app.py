from flask import Flask, jsonify, render_template, request
from lib_hub.library import Library, fine_tier, validate_isbn

app = Flask(__name__, template_folder="../webapp/templates")
library = Library()
books = {}
borrowed_books = {}


def reset_data():
    library.member_loans.clear()
    books.clear()
    borrowed_books.clear()


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/books")
def create_book():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    isbn = data.get("isbn")
    author = data.get("author")
    total_copies = data.get("total_copies")

    if not title or not isinstance(title, str) or not title.strip():
        return jsonify({"error": "title is required"}), 400
    if not author or not isinstance(author, str) or not author.strip():
        return jsonify({"error": "author is required"}), 400
    if type(total_copies) is not int or total_copies < 1:
        return jsonify({"error": "total_copies must be a positive integer"}), 400

    try:
        validate_isbn(isbn)
    except ValueError as err:
        return jsonify({"error": str(err)}), 400

    books[isbn] = {
        "title": title.strip(),
        "isbn": isbn,
        "author": author.strip(),
        "available_copies": total_copies,
    }
    return jsonify(books[isbn]), 201


@app.get("/books")
def get_all_books():
    return jsonify(list(books.values())), 200


@app.get("/books/<isbn>")
def get_single_book(isbn):
    book = books.get(isbn)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200


@app.post("/members/<member_id>/borrow")
def borrow(member_id):
    data = request.get_json(silent=True) or {}
    isbn = data.get("isbn")
    if not isbn:
        return jsonify({"error": "isbn is required"}), 400

    book = books.get(isbn)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    if book["available_copies"] <= 0:
        return jsonify({"error": "No copies available"}), 400

    try:
        library.borrow_book(member_id, isbn)
    except ValueError as err:
        return jsonify({"error": str(err)}), 400

    book["available_copies"] -= 1
    borrowed_books.setdefault(member_id, []).append(isbn)
    return jsonify({"isbn": isbn, "available_copies": book["available_copies"]}), 200


@app.post("/members/<member_id>/return")
def return_book(member_id):
    data = request.get_json(silent=True) or {}
    isbn = data.get("isbn")
    if not isbn:
        return jsonify({"error": "isbn is required"}), 400

    book = books.get(isbn)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    member_items = borrowed_books.get(member_id, [])
    if isbn not in member_items:
        return jsonify({"error": "Book not borrowed by this member"}), 400

    member_items.remove(isbn)
    library.member_loans[member_id] = max(0, library.member_loans.get(member_id, 1) - 1)
    book["available_copies"] += 1
    return jsonify({"isbn": isbn, "available_copies": book["available_copies"]}), 200


@app.get("/members/<member_id>/fines")
def member_fines(member_id):
    days_param = request.args.get("days_overdue")
    if days_param is None:
        return jsonify({"error": "days_overdue is required"}), 400
    try:
        days = int(days_param)
        tier = fine_tier(days)
    except ValueError as err:
        return jsonify({"error": str(err)}), 400

    return jsonify({"member_id": member_id, "days_overdue": days, "tier": tier}), 200


if __name__ == "__main__":
    app.run(port=5000)