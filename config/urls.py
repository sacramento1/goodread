# from xml.etree.ElementInclude import include
from django.urls import include

from django.contrib import admin
from django.urls import path

from config.views import home_page
from django.conf.urls.static import static
from django.conf import settings

app_name = "goodread"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('users/', include("apps.users.urls")),
    # path('books/', include("apps.books.books")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
