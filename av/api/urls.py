from django.conf.urls import url
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (FilialViewSet, EmpresaViewSet, PainelGeralViewSet, DetalheIndicadorViewSet, NotaFilialViewSet,
                    NotaViewSet, CalculoMensal)



router = SimpleRouter()
router.register('filial', FilialViewSet)
router.register('empresa', EmpresaViewSet)
router.register('painelgeral', PainelGeralViewSet)
router.register('detalheindicador', DetalheIndicadorViewSet)
router.register('notafilial', NotaFilialViewSet)
router.register('nota', NotaViewSet)


urlpatterns = [
    path('calcular/', CalculoMensal.as_view())
]

