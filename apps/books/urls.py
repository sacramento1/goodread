from django.urls import path

from apps.books.views import AddReviewView, BookListView, BookDetailView, review_delete, review_update

app_name = "books"

urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book-detail"),
    path('<int:pk>', AddReviewView.as_view(), name="add-review"),
    path('review-update/<int:pk>', review_update, name="review-update"),
    path('review-delete/<int:pk>', review_delete, name="review-delete"),
    # path('genre/<str:genre>/', GenreView.as_view(), name='book-genre'),
    # path('<pk>/', AuthorView.as_view(), name="book-detail"),
    # path('<pk>/', GenreView.as_view(), name="book-detail"),
]