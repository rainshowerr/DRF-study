from django.urls import path, include
from .views import HelloAPI, booksAPI, bookAPI, BookAPI, BooksAPI, BooksAPIMixins, BookAPIMixins, BooksAPIGenerics, BookAPIGenerics, BookViewSet
from rest_framework import routers

# urlpatterns = [
# 	path("hello/", HelloAPI),
#     # 함수형 뷰
#     path("fbv/books/", booksAPI),
#     path("fbv/book/<int:bid>/", bookAPI),
#     # 클래스형 뷰 (as_view() 사용)
#     path("cbv/books/", BooksAPI.as_view()),
#     path("cbv/book/<int:bid>/", BookAPI.as_view()),
#     # mixin
#     path("mixin/books/", BooksAPIMixins.as_view()),
#     path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
#     # generic
#     path("generic/books/", BooksAPIGenerics.as_view()),
#     path("generic/book/<int:bid>/", BookAPIGenerics.as_view()),
# ]

router = routers.SimpleRouter()
router.register('books', BookViewSet)
urlpatterns = router.urls