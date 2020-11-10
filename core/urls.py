from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from . import views


urlpatterns = [
   path('', views.index, name='home'),
   # Matches any html file
   #re_path(r'^[media]', views.pages, name='pages'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
