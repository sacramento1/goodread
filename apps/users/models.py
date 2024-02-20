from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, CharField, ForeignKey, CASCADE, ManyToManyField

from apps.shared.models import AbstractModel


class User(AbstractUser):
    avatar = ImageField(upload_to="users/avatar/%Y/%m/%d", default="avatar_users.png")
    middle_name = CharField(max_length=128, null=True, blank=True)


class BookShelf(AbstractModel):
    name = CharField(max_length=128)
    user = ForeignKey("users.User", CASCADE, 'bookshelf')
    books = ManyToManyField("books.Book", "bookshelves")
