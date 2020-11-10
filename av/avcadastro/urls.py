from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('filialnota/novo/', views.notafilialCreate, name="novo-av-notafinal"),
    path('filialnota/update/<int:id>/', views.notafilialedit, name="update-av-notafinal"),
    path('filialnota/delete/<int:id>/', views.notafilialdelete, name="delete-av-notafinal"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)