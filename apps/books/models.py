from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CharField, TextField, SlugField, TextChoices, IntegerField, ImageField, URLField, \
    ManyToManyField, ForeignKey, CASCADE
from django.forms import DateField

from apps.shared.models import AbstractModel


class LanguageChoice(TextChoices):
    ENGLISH = "en", "English"
    FRANCE = "fr", "France"
    RUSSIAN = "ru", "Russian"
    ARABIC = "ab", "Arabic"
    UZBEK = "uz", "Uzbek"
0

class Book(AbstractModel):
    title = CharField(max_length=128)
    slug = SlugField(unique=True)
    description = TextField()
    published = DateField()
    isbn = CharField(max_length=128,unique=True)
    language = CharField(max_length=7, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH)
    page = IntegerField()
    cover = ImageField(upload_to="books/cover/%Y/%m/%d", default="default_book.png")
    genre = ManyToManyField("books.BookGenre","books")
    authors = ManyToManyField("books.BookAuthor", "books")

    def __str__(self) -> str:
        return self.title


class BookAuthor(AbstractModel):
    first_name = CharField(max_length=56)
    last_name = CharField(max_length=56)
    birthdate = DateField()
    website = URLField()
    avatar = ImageField(upload_to="authors/avatar/%Y/%m/%d", default="avatar.png")
    about = TextField()

    def __str__(self) -> str:
        return F"{self.last_name} {self.first_name}"

class BookGenre(AbstractModel):
    name = CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

class BookReview(AbstractModel):
    body = TextField()
    rating = IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    like_count = IntegerField(default=0)
