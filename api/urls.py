from django.urls import path, include
from api.books.urls import urlpatterns as books_urls
from api.auth_user.urls import urlpatterns as auth_user_urls


urlpatterns = [
    path('', include(auth_user_urls)),
    path('', include(books_urls)),
]
