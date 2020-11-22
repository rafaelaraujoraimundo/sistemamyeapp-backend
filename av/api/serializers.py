from rest_framework import serializers
from django.db.models import Avg

from av.avcadastro.models import Indicador, PainelGeral, DetalheIndicador, NotaFilial, Nota
from core.models import Filial, Empresa, CustomUsuario


class FilialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filial
        fields = (
            'id',
            'codfilial',
            'nomefilial',
            'cnpj',
            'idempresa',
            'criadopor'
        )

    """def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A Avalição precisa ser entre 1 e 5')
    """


class EmpresaSerializer(serializers.ModelSerializer):
    # Nested RelantionShip
    filiais = FilialSerializer(many=True, read_only=True)                                  

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
            'filiais',
            'criadopor'
        )
        

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
            'criadopor'
        )


class DetalheIndicadorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DetalheIndicador
        fields = (
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
            'criadopor'
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


class UsuarioSerializer(serializers.ModelSerializer):
    filial = FilialSerializer(source='idfilial')
    empresa = EmpresaSerializer(source='idempresa')
    
    class Meta:
        model = CustomUsuario
        fields = (
            'email',
            'first_name',
            'last_name',
            'fone',
            'perfil',
            'idmodulos',
            'filial',
            'empresa',
            
        )