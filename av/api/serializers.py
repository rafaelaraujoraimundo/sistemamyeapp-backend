from rest_framework import serializers
from django.db.models import Avg

from av.avcadastro.models import Indicador, PainelGeral, DetalheIndicador, NotaFilial, Nota
from core.models import Filial, Empresa, CustomUsuario


class EmpresaSerializer(serializers.ModelSerializer):
    # Nested RelantionShip
    #filiais = FilialSerializer(many=True, read_only=True, required=False)                                  

    # HyperLInked Related Field
    #idempresas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # Primary Key Related Field
    #filiais = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Empresa
        fields = (
            'id',
            'codempresa',
            'nomeempresa',
            'logoempresa',
            'ativo',
            'criadopor'
        )


class FilialSerializer(serializers.ModelSerializer):
    
    empresa = EmpresaSerializer(source='idempresa', required=False)
    
    class Meta:
        model = Filial
        fields = (
            'id',
            'codfilial',
            'nomefilial',
            'cnpj',
            'idempresa',
            'criadopor',
            'empresa'
        )

    """def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A Avalição precisa ser entre 1 e 5')
    """

     
class IndicadorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicador
        fields = (
            'id',
            'idempresa',
            'idfilial',
            'codigo',
            'descricao',
            'peso',
            'modo',
            'Inverso',
            'criadopor'
        )


class PainelGeralSerializer(serializers.ModelSerializer):
    indicadorPrincipal = IndicadorSerializer(source='idindicador', required=False)
    
    class Meta:
        model = PainelGeral
        fields = (
            'idempresa',
            'idfilial',
            'periodo',
            'idindicador',
            'orcadometa',
            'realizado',
            'peso',
            'pontuacao',
            'criadopor',
            'indicadorPrincipal',
        )


class DetalheIndicadorSerializer(serializers.ModelSerializer):
    indicador = IndicadorSerializer(source='idindicador', required=False)
    
    class Meta:
        model = DetalheIndicador
        fields = (
            'id',
            'idempresa',
            'idfilial',
            'periodo',
            'idindicador',
            'descricao',
            'meta',
            'resultado',
            'modoindicador',
            'incluso',
            'Inverso',
            'criadopor',
            'indicador'
        )


class NotaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nota
        fields = (
            'nota',
            'inicio',
            'fim',
            'cor',
            'criadopor'
        )


class NotaFilialSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = NotaFilial
        fields = (
            'idempresa',
            'idfilial',
            'periodo',
            'nota',
            'criadopor',
        )


class UsuarioSerializer(serializers.ModelSerializer):
    filial = FilialSerializer(source='idfilial', required=False)
    empresa = EmpresaSerializer(source='idempresa', required=False)
    
    class Meta:
        model = CustomUsuario
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'fone',
            'perfil',
            'idmodulos',
            'filial',
            'empresa',
            'password',
            'idfilial',
            'idempresa'
        )

    def create(self, validated_data):
        user = super(UsuarioSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        
        if self.initial_data["admin"] == 'true':
            user.is_superuser = True
        else:
            user.is_superuser = False
        user.save()
        return user
