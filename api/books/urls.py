from django.urls import path, include
from api.books.views.books import BooksListAPIView, BooksRetrieveAPIView

urlpatterns = [
    path('books/', BooksListAPIView.as_view(), name='books-list'),
    path('books/<str:slug>/', BooksRetrieveAPIView.as_view(), name='books-detail'),
]
