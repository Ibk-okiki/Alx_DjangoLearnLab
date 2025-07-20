# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based view (FBV): Lists all books
    path('books/', list_books, name='list_books'),

    # Class-based view (CBV): Shows a specific library by primary key (ID)
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
