"""sistemaRR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from rest_auth import urls
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.contrib.auth.views import PasswordResetForm

import av
from av.api.urls import router

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Sistema MyeApp",
        default_version='v1',
        description="APIs de Integração",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@myeapp.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


def empty_view(args):
    pass


urlpatterns = [
                  path('admin/', admin.site.urls),  # Django admin route 
                  path('api/v1/', include(router.urls)),
                  path('api/', include(av.api.urls)),
                  path('accounts/', include('rest_framework.urls')),
                  path('auth/', include('rest_auth.urls')),
                  path('auth/refresh-token/', refresh_jwt_token),
                  path('auth//<uidb64>/<token>/', empty_view, name='password_reset_confirm'),
                  url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                      name='schema-json'),
                  url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    Authenticação antiga
    path('auth/', include('rest_framework.urls')),
   
    path('api-token-auth/', obtain_auth_token_user, name='api_token_auth'),
    path("", include("authentication.urls")),  # Auth routes - login / register
    """
