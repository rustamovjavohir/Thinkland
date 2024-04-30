from rest_framework import serializers

from apps.auth_user.models import Authors
from utils.serializers import FilteredActiveListSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = (
            'id',
            'name',
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
        list_serializer_class = FilteredActiveListSerializer
