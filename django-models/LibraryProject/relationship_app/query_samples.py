import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data (optional but useful for testing)
author = Author.objects.create(name="Wole Soyinka")
book1 = Book.objects.create(title="The Lion and the Jewel", author=author)
book2 = Book.objects.create(title="Death and the King's Horseman", author=author)

library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)

librarian = Librarian.objects.create(name="Grace", library=library)

# --- Required Queries ---

# 1. ✅ Query all books by a specific author
author_name = "Wole Soyinka"
author = Author.objects.get(name=author_name)  # <-- REQUIRED LINE
books_by_author = Book.objects.filter(author=author)  # <-- REQUIRED LINE
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# 2. ✅ List all books in a library using Library.objects.get(name=...)
library_name = "Central Library"
lib = Library.objects.get(name=library_name)
print(f"\nBooks in {library_name}:")
for book in lib.books.all():
    print(book.title)

# 3. ✅ Retrieve the librarian for a library
print(f"\nLibrarian of {library_name}:")
print(lib.librarian.name)
