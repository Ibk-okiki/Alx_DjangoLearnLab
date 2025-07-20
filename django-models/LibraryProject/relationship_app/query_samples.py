import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample Data Creation
author1 = Author.objects.create(name="Chinua Achebe")
book1 = Book.objects.create(title="Things Fall Apart", author=author1)
book2 = Book.objects.create(title="No Longer at Ease", author=author1)

library1 = Library.objects.create(name="National Library")
library1.books.set([book1, book2])  # Add books to library

librarian1 = Librarian.objects.create(name="John Doe", library=library1)


# ✅ 1. Query all books by a specific author
books_by_achebe = Book.objects.filter(author__name="Chinua Achebe")
print("Books by Chinua Achebe:")
for book in books_by_achebe:
    print(f"- {book.title}")

# ✅ 2. List all books in a library
books_in_library = library1.books.all()
print(f"\nBooks in {library1.name}:")
for book in books_in_library:
    print(f"- {book.title}")

# ✅ 3. Retrieve the librarian for a library
librarian = library1.librarian
print(f"\nLibrarian at {library1.name}: {librarian.name}")
