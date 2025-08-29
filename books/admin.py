from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'publication_date', 'created_at']
    list_filter = ['author', 'publication_date', 'created_at']
    search_fields = ['title', 'author', 'isbn']
    ordering = ['-created_at']
