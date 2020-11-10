from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.response import Response

from av.avcadastro.models import Filial, Empresa
from .serializers import EmpresaSerializer, FilialSerializer


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


class FilialViewSet(
    mixins.ListModelMixin,
    CreateModelMixinUser,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class EmpresaViewSet(
    mixins.ListModelMixin,
    CreateModelMixinUser,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


