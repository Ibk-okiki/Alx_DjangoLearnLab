from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Optional: Keep simple list view
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLs for full CRUD
    path('', include(router.urls)),
]


