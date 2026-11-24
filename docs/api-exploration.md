# API Manual Exploration Notes (Lab 12)

Base URL: `http://127.0.0.1:5000`

## 1. POST /books (Valid Request)
- **Request:** `POST /books`
- **Body:** `{"title": "Clean Code", "isbn": "9780132350884", "author": "Robert C. Martin", "total_copies": 2}`
- **Status:** `201 Created`
- **Response:** `{"available_copies": 2, "author": "Robert C. Martin", "isbn": "9780132350884", "title": "Clean Code"}`

## 2. POST /books (Invalid - Missing `title`)
- **Request:** `POST /books`
- **Body:** `{"isbn": "9780132350884", "author": "Robert C. Martin", "total_copies": 2}`
- **Status:** `400 Bad Request`
- **Response:** `{"error": "title is required"}`

## 3. POST /books (Invalid - Wrong Type for `total_copies`)
- **Request:** `POST /books`
- **Body:** `{"title": "Clean Code", "isbn": "9780132350884", "author": "Robert C. Martin", "total_copies": "two"}`
- **Status:** `400 Bad Request`
- **Response:** `{"error": "total_copies must be a positive integer"}`

## 4. GET /books/<isbn>
- **Request:** `GET /books/9780132350884`
- **Status:** `200 OK` (or `404 Not Found` if ISBN does not exist)

## 5. POST /members/<member_id>/borrow
- **Request:** `POST /members/M1/borrow`
- **Body:** `{"isbn": "9780132350884"}`
- **Status:** `200 OK`

## 6. POST /members/<member_id>/return
- **Request:** `POST /members/M1/return`
- **Body:** `{"isbn": "9780132350884"}`
- **Status:** `200 OK`

## 7. GET /members/<member_id>/fines
- **Request:** `GET /members/M1/fines?days_overdue=10`
- **Status:** `200 OK`
- **Response:** `{"days_overdue": 10, "member_id": "M1", "tier": "Medium"}`