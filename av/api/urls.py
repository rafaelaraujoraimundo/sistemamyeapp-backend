from django.conf.urls import url
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (FilialViewSet, EmpresaViewSet, PainelGeralViewSet, DetalheIndicadorViewSet, NotaFilialViewSet,
                    NotaViewSet, CalculoMensal, IndicadorPrincipalViewSet, Dashboard, UserViewSet)

router = SimpleRouter()
router.register('filial', FilialViewSet)
router.register('empresa', EmpresaViewSet)
router.register('painelgeral', PainelGeralViewSet)
router.register('detalheindicador', DetalheIndicadorViewSet)
router.register('notafilial', NotaFilialViewSet)
router.register('nota', NotaViewSet)
router.register('indicadorPrincipial', IndicadorPrincipalViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('calcular/', CalculoMensal.as_view()),
    path('dashboard/', Dashboard.as_view()),
]

