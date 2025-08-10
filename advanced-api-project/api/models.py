from django.db import models
from datetime import date

# Author model represents a book author in the database
class Author(models.Model):
    name = models.CharField(max_length=255)  # Name of the author

    def __str__(self):
        return self.name


# Book model represents a published book
# Has a one-to-many relationship with Author (one author can have many books)
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year book was published
    author = models.ForeignKey(
        Author,
        related_name='books',  # This allows reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
      
