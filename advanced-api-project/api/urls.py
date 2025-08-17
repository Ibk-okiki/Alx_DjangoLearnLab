from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView
from .views import ListView, UpdateView, DeleteView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create", ListView.as_view(), name="book-create"),
    path("books/update/<int:pk>", UpdateView.as_view(), name="book-update"),
    path("books/delete/<int:pk>", DeleteView.as_view(), name="book-delete"),
]
