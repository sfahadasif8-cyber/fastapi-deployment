from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "API is healthy"}

def test_get_books():
    response = client.get("/books")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_book():
    response = client.post(
        "/books",
        json={
            "title": "Test Book",
            "author": "Test Author"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Test Book"
    assert data["author"] == "Test Author"
    assert "id" in data

def test_get_book_by_id():
    # First, create a book to ensure there is one to retrieve
    create_response = client.post(
        "/books",
        json={
            "title": "Another Test Book",
            "author": "Another Test Author"
        }
    )
    book_id = create_response.json()["id"]

    # Now, retrieve the book by its ID
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == book_id
    assert data["title"] == "Another Test Book"
    assert data["author"] == "Another Test Author"

def test_update_book():
    # First, create a book to ensure there is one to update
    create_response = client.post(
        "/books",
        json={
            "title": "Book to Update",
            "author": "Author Before Update"
        }
    )
    book_id = create_response.json()["id"]

    # Now, update the book's title and author
    response = client.put(
        f"/books/{book_id}",
        json={
            "title": "Updated Book Title",
            "author": "Updated Author"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == book_id
    assert data["title"] == "Updated Book Title"
    assert data["author"] == "Updated Author"

def test_delete_book():
    # First, create a book to ensure there is one to delete
    create_response = client.post(
        "/books",
        json={
            "title": "Book to Delete",
            "author": "Author to Delete"
        }
    )
    book_id = create_response.json()["id"]

    # Now, delete the book by its ID
    response = client.delete(f"/books/{book_id}")

    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted successfully"}

    # Verify that the book no longer exists
    get_response = client.get(f"/books/{book_id}")
    assert get_response.status_code == 404

def test_get_nonexistent_book():
    response = client.get("/books/9999")  # Assuming 9999 is a non-existent ID

    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_update_nonexistent_book():
    response = client.put(
        "/books/9999",  # Assuming 9999 is a non-existent ID
        json={
            "title": "Non-existent Book",
            "author": "No Author"
        }
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_delete_nonexistent_book():
    response = client.delete("/books/9999")  # Assuming 9999 is a non-existent ID

    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

def test_create_book_invalid_data():
    response = client.post(
        "/books",
        json={
            "title": "",  # Invalid title (empty)
            "author": "Author with Invalid Title"
        }
    )

    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()

def test_update_book_invalid_data():
    # First, create a book to ensure there is one to update
    create_response = client.post(
        "/books",
        json={
            "title": "Book to Update Invalid",
            "author": "Author Before Update"
        }
    )
    book_id = create_response.json()["id"]

    # Now, attempt to update the book with invalid data
    response = client.put(
        f"/books/{book_id}",
        json={
            "title": "",  # Invalid title (empty)
            "author": "Updated Author"
        }
    )

    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()