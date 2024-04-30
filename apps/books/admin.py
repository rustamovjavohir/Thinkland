from django.contrib import admin
from apps.books.models import Books, BookImages


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'first_image', 'updated_at')
    search_fields = ('name', 'author')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(BookImages)
class BookImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
