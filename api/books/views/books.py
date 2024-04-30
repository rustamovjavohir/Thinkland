from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.books.filters import BooksFilter
from api.books.paginations import BooksPagination
from apps.books.models import Books
from api.books.serializers.books import BooksSerializer
from utils.mixins import HandleExceptionMixin
from utils.responses import Response


class BooksListAPIView(HandleExceptionMixin, ListAPIView):
    queryset = Books.objects.book_with_images()
    serializer_class = BooksSerializer
    pagination_class = BooksPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BooksFilter
    search_fields = ['$name', '$authors__name', '$published']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BooksRetrieveAPIView(HandleExceptionMixin, RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data=serializer.data)
