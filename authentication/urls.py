
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
