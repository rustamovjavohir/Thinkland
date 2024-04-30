from rest_framework import serializers
from apps.books.models import BookImages


class BookImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImages
        fields = (
            'id',
            'image',
            'alt',
            'title',
            'created_at',
            'updated_at',
            'is_active'
        )
        read_only_fields = (
            'id',
            'created_at',
            'updated_at',
            'is_active'
        )
