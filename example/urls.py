from django.urls import path

from example.views import booksAPI, bookAPI, BooksAPI, BookAPI

urlpatterns = [
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view())
]