from django.db import models
from django.utils import timezone

class Author(models.Model):
    """
    Represents an author of books.

    Fields:
        name (str): The author's full name.
    """
    name = models.CharField(max_length=255, help_text="Full name of the author")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """
    Represents a book written by an Author.

    Fields:
        title (str): Title of the book.
        publication_year (int): Year the book was published.
        author (FK): Link to the Author (one author → many books).
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",  # enables author.books.all() and powers nested serialization
    )

    class Meta:
        ordering = ["-publication_year", "title"]
        constraints = [
            # simple example: prevent year 0 (historical edge case)
            models.CheckConstraint(
                check=models.Q(publication_year__gte=1),
                name="book_publication_year_gte_1",
            )
        ]

    def __str__(self) -> str:
        return f"{self.title} ({self.publication_year})"
