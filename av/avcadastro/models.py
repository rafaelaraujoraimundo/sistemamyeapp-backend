from django.db import models
from rest_framework import request

from core.models import Empresa, Filial
from sistemaRR import settings


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    criadopor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
        ordering = ['id']


class Indicador(Base):
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, related_name='empresaindicador', null=False)
    CHOICE_MODO = (
        ("CAL", "CALCULO"),
        ("CON", "CONTAR"),
        ("UNI", "UNITARIO")
    )
    idfilial = models.ForeignKey(Filial, models.DO_NOTHING, related_name='filialindicador', blank=False, null=False)
    codigo = models.IntegerField(default='1')
    descricao = models.CharField(max_length=100, blank=False, null=False)
    peso = models.DecimalField(max_digits=18, decimal_places=2, blank=False, null=False)
    modo = models.CharField(max_length=3, choices=CHOICE_MODO, blank=False, null=False)
    Inverso = models.BooleanField('Calculo Inverso?', default=False)
    
    class Meta:
        managed = True
        db_table = 'av_indicador'
        unique_together = ('idfilial', 'idempresa', 'codigo')

    def __str__(self):
        return self.descricao
    

class PainelGeral(Base):
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, related_name='empresaspainel', null=False)
    periodo = models.CharField(max_length=6, blank=False, null=False)
    idfilial = models.ForeignKey(Filial, models.DO_NOTHING, related_name='filial', blank=False, null=False)
    idindicador = models.ForeignKey(Indicador, models.DO_NOTHING, related_name='painelindicador', null=False)
    orcadometa = models.DecimalField(max_digits=18, decimal_places=2, blank=False, null=False)
    realizado = models.DecimalField(max_digits=18, decimal_places=2, blank=False, null=False)
    peso = models.DecimalField(max_digits=18, decimal_places=2, blank=False, null=False)
    pontuacao = models.DecimalField(max_digits=18, decimal_places=2, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'av_painelgeral'
        unique_together = ('idfilial', 'idempresa', 'idindicador', 'periodo')

    def __str__(self):
        return self.periodo + ' - ' + self.idindicador.descricao


class DetalheIndicador(Base):
    CHOICE_MODO = (
        ("CSM", "CALCULO SOMA"),
        ("CSB", "CALCULO SUBTRAI"),
        ("CMU", "CALCULO MULTIPLICA"),
        ("CDI", "CALCULO DIVIDE"),
        ("UNI", "UNITARIO"),
        ("CON", "CONTAR"),
        ("NDA", "NAO FAZ PARTE")
    )
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, related_name='empresasdetalheindicador', null=False)
    periodo = models.CharField(max_length=6, blank=False, null=False)
    idfilial = models.ForeignKey(Filial, models.DO_NOTHING, related_name='filialdetalheindicador', blank=False, null=False)
    idindicador = models.ForeignKey(Indicador, models.DO_NOTHING, related_name='indicador', blank=False, null=False)
    descricao = models.CharField(max_length=100, blank=False, null=False, unique=True)
    meta = models.DecimalField(max_digits=18, decimal_places=2, blank=False, null=False)
    resultado = models.DecimalField(max_digits=18, decimal_places=2, blank=False, null=False)
    modoindicador = models.CharField(max_length=3, choices=CHOICE_MODO, blank=False, null=False)
    incluso = models.BooleanField('Incluso no Calculo?', default=True)
    Inverso = models.BooleanField('Calculo Inverso?', default=False)
    
    class Meta:
        managed = True
        db_table = 'av_detalheindicador'

    def __str__(self):
        return self.descricao


class NotaFilial(Base):
    CHOICE_NOTA = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E")
    )
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, related_name='empresasnota', null=False)
    idfilial = models.ForeignKey(Filial, models.DO_NOTHING, related_name='filialnota', blank=False, null=False)
    periodo = models.CharField(max_length=6, blank=False, null=False)
    nota = models.CharField(max_length=1, choices=CHOICE_NOTA, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'av_notafilial'
        unique_together = ('idfilial', 'periodo')
        
    
        
    def __str__(self):
        return self.nota


class Nota(Base):
    CHOICE_NOTA = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E")
    )
    CHOICE_COR = (
        ("BLUE", "AZUL"),
        ("GREEN", "VERDE"),
        ("Gold", "AMARELO"),
        ("ORANGE", "LARANJA"),
        ("RED", "VERMELHO")
    )
    nota = models.CharField(max_length=1, choices=CHOICE_NOTA, blank=False, null=False, unique=True)
    inicio = models.DecimalField(max_digits=99, decimal_places=2, blank=False, null=False)
    fim = models.DecimalField(max_digits=99, decimal_places=2, blank=False, null=False)
    cor = models.CharField(max_length=14, choices=CHOICE_COR, blank=False, unique=True, default='RED')

    class Meta:
        managed = True
        db_table = 'av_nota'

    def __str__(self):
        return self.nota


