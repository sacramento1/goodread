from django.urls import path

from apps.books.views import BookListView, BookDetailView, GenreView

app_name = "books"

urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book-detail"),
    path('genre/<str:genre>/', GenreView.as_view(), name='book-genre'),
    # path('<pk>/', AuthorView.as_view(), name="book-detail"),
    # path('<pk>/', GenreView.as_view(), name="book-detail"),
]