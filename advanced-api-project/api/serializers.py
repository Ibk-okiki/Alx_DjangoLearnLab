from datetime import date
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """Serializes Book instances.

    Includes custom validation to ensure `publication_year` is not in the future.
    """

    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

    def validate_publication_year(self, value: int) -> int:
        """Ensure the publication year is not in the future."""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future (>{current_year})."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """Serializes Author instances with nested books.

    The `books` field is read‑only and populated dynamically via the `related_name`
    on Book.author (i.e., `author.books.all()`). If you later want to support
    creating/updating books within the author payload, switch this to a writable
    nested serializer and override `create`/`update`.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
