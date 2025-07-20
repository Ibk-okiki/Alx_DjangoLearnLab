import os
import django

# Setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Create Sample Data (optional if using shell instead) ---
author = Author.objects.create(name="Wole Soyinka")
book1 = Book.objects.create(title="The Lion and the Jewel", author=author)
book2 = Book.objects.create(title="Death and the King's Horseman", author=author)

library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)

librarian = Librarian.objects.create(name="Grace", library=library)

# --- Queries ---

# 1. Query all books by a specific author
print("Books by Wole Soyinka:")
for book in Book.objects.filter(author__name="Wole Soyinka"):
    print(book.title)

# 2. List all books in a library
print("\nBooks in Central Library:")
for book in library.books.all():
    print(book.title)

# 3. Retrieve the librarian for a library
print("\nLibrarian of Central Library:")
print(library.librarian.name)
