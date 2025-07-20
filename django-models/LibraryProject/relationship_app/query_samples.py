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
