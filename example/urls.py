from django.urls import path, include
from .views import HelloAPI, bookAPI, booksAPI, BooksAPI, BookAPI, BooksAPIMixins, BookAPIMixins, BooksAPIGenerics, BookAPIGenerics

from rest_framework import routers
from .views import BookViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
    path('mixin/books/', BooksAPIMixins.as_view()),
    path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
    path('generics/books/', BooksAPIGenerics.as_view()),
    path('generics/book/<int:bid>/', BookAPIGenerics.as_view()),
    path('', include(router.urls)),

]