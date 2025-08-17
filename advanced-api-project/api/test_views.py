from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Create test books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2001)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2005)

        # URLs
        self.list_url = reverse("book-list")     # books/
        self.create_url = reverse("book-list")   # books/
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book1.id])

    # ------------------------
    # CRUD Tests
    # ------------------------

    def test_create_book(self):
        data = {"title": "New Book", "author": "Author C", "publication_year": 2020}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest("id").title, "New Book")

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_update_book(self):
        data = {"title": "Updated Title", "author": "Author A", "publication_year": 2001}
        response = self.client.put(self.update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # ------------------------
    # Filtering, Searching, Ordering
    # ------------------------

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Author A"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author A")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_order_books_by_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

    # ------------------------
    # Permissions & Auth
    # ------------------------

    def test_unauthenticated_user_cannot_create(self):
        self.client.logout()
        data = {"title": "Unauthorized Book", "author": "Anon", "publication_year": 2022}
        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
  
