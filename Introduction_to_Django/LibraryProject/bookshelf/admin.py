from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown in list
    search_fields = ('title', 'author')                     # enables search box
    list_filter = ('publication_year',)                     # adds filter by year
