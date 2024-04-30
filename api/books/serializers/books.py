from rest_framework import serializers
from apps.books.models import Books
from utils.serializers import FilteredActiveListSerializer
from api.auth_user.serializers.author import AuthorSerializer
from api.books.serializers.images import BookImagesSerializer


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    images = BookImagesSerializer(many=True)

    class Meta:
        model = Books
        fields = (
            'id',
            'name',
            'slug',
            'authors',
            'images',
            'published',
            'description',
            'created_at',
            'updated_at',
            'is_active'
        )
        read_only_fields = (
            'id',
            'slug',
            'created_at',
            'updated_at',
            'is_active'
        )
        list_serializer_class = FilteredActiveListSerializer
