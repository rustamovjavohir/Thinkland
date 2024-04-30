from django_filters import CharFilter
from django_filters.rest_framework import FilterSet
from apps.books.models import Books


class BooksFilter(FilterSet):
    class Meta:
        model = Books
        fields = {
            'authors': ["exact"],
            'published': ["exact"],
        }
