from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (FilialViewSet, EmpresaViewSet)

router = SimpleRouter()
router.register('filial', FilialViewSet)
router.register('empresa', EmpresaViewSet)

urlpatterns = [
    #path('', FileUploadView.as_view())
]

