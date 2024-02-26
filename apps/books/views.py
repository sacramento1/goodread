from msilib.schema import ListView
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View

from apps.books.forms import AddBookReviewForm
from apps.books.models import Book, BookReview
from apps.users.models import User
from django.core.paginator import Paginator


class BookListView(View):
    def get(self, request):
        queryset = Book.objects.all()
        param = request.GET.get("q", None)

        if param is not None:
            queryset = queryset.filter(title__icontains=param)
        context = {
            "books": queryset,
            "param": param
        }
        size = request.GET.get("size", 3)
        page = request.GET.get("page", 1)

        paginator = Paginator(queryset, size)
        page_obj = paginator.page(page)

        return render(request, "books/book-list.html", context={"page_obj": page_obj, "num_pages":paginator.num_pages})


class BookDetailView(View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        form = AddBookReviewForm()
        context = {
            "book": book,
            "form": form
        }
        return render(request, "books/book-detail.html", context=context)


class AddReviewView(View):
    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        user = User.objects.get(username=request.user.username)
        form = AddBookReviewForm(request.POST)
        if form.is_valid():
            BookReview.objects.create(
                user=user,
                book=book,
                body=form.cleaned_data.get("body"),
                rating=form.cleaned_data.get("rating")
            )
            return redirect(reverse("books:book-detail", kwargs={"slug": book.slug}))
        else:
            context = {
                "book": book,
                "form": form
            }
            return render(request, "books/book-detail.html", context=context)

def review_update(request, pk: int):
    review = BookReview.objects.get(pk=pk)
    if request.method == "POST":
        form = AddBookReviewForm(data=request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "post successfully updated")
            return redirect(reverse('books:book-detail', kwargs={"pk":review.id}))
        else:
            return render(request, "review_update.html", {"form": form})
    else:
        form = AddBookReviewForm(instance=review)
        return render(request, "review_update.html", {"form": form})

def review_delete(requet, pk):
    review = get_object_or_404(BookReview, pk=pk)
    if requet.method == "POST":
        messages.success(requet, "Review successfully deleted")
        review.delete()
        return redirect(reverse('books:book-list', kwargs={"username": requet.user.username}))
    else:
        return render(requet, "review_delete.html", {"review": review})
    

class AddBookView(View):
    def post(self, request, pk):
        pass




# class GenreView(ListView):
#     model = Book
#     template_name = 'books/book-list.html'
#     context_object_name = 'books'

#     def get_queryset(self):
#         genre = BookGenre.self.kwargs['romantic']
#         queryset = Book.objects.filter(genre=genre)
#         return queryset
    
# class AuthorView()