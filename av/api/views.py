from rest_framework import viewsets, status, request
from rest_framework import mixins
from rest_framework.response import Response

from av.avcadastro.models import Filial, Empresa, Indicador, PainelGeral, DetalheIndicador, NotaFilial, Nota
from .serializers import EmpresaSerializer, FilialSerializer, IndicadorSerializer, PainelGeralSerializer, \
    DetalheIndicadorSerializer, NotaFilialSerializer, NotaSerializer


class CreateModelMixinUser(mixins.CreateModelMixin):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        request.data.update({'criadopor': request.user.id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.criadopor = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CreateModelMixinUserFilialEmpresa(mixins.CreateModelMixin):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        request.data.update({'criadopor': request.user.id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.criadopor = request.user
        serializer.idempresa = request.user.idempresa
        serializer.idfilial = request.user.idfilial
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListModelMixinFilialEmpresa(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(idempresa=request.user.idempresa, idfilial=request.user.idfilial)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ListModelMixinEmpresa(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(id=request.user.idempresa.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FilialViewSet(
    ListModelMixinEmpresa,
    CreateModelMixinUser,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class EmpresaViewSet(
    ListModelMixinEmpresa,
    CreateModelMixinUser,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class PainelGeralViewSet(
    ListModelMixinFilialEmpresa,
    CreateModelMixinUserFilialEmpresa,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = PainelGeral.objects.all()
    serializer_class = PainelGeralSerializer


class DetalheIndicadorViewSet(
    ListModelMixinFilialEmpresa,
    CreateModelMixinUserFilialEmpresa,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = DetalheIndicador.objects.all()
    serializer_class = DetalheIndicadorSerializer
    

class NotaFilialViewSet(
    ListModelMixinFilialEmpresa,
    CreateModelMixinUserFilialEmpresa,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = NotaFilial.objects.all()
    serializer_class = NotaFilialSerializer
    

class NotaViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
