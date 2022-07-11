from django.urls import path
from rest_framework import routers

from example.views import booksAPI, bookAPI, BooksAPI, BookAPI, BooksAPIMixins, BookAPIMixins, BooksAPIGenerics, \
    BookAPIGenerics, BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)

# urlpatterns = [
#     path('fbv/books/', booksAPI),
#     path('fbv/book/<int:bid>/', bookAPI),
#     path('cbv/books/', BooksAPI.as_view()),
#     path('cbv/book/<int:bid>/', BookAPI.as_view()),
#     path('mixin/books/', BooksAPIMixins.as_view()),
#     path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
#     path('generics/books/', BooksAPIGenerics.as_view()),
#     path('generics/book/<int:bid>/', BookAPIGenerics.as_view()),
#
# ]

urlpatterns = router.urls