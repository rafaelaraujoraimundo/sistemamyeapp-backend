from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from stdimage.models import StdImageField

from sistemaRR import settings

"""
Cadastro de Empresas e Filiais
"""


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    criadopor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
        ordering = ['id']


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class Empresa(Base):
    codempresa = models.CharField(db_column='Codempresa', unique=True, max_length=10, blank=False, null=False)
    nomeempresa = models.CharField(db_column='Nomeempresa', max_length=100, blank=False, null=False)
    logoempresa = StdImageField('Imagem', upload_to='logo', variations={'thumb': (166, 173)})

    class Meta:
        managed = True
        db_table = 'empresa'
        ordering = ['id']

    def __str__(self):
        return self.nomeempresa


class Filial(Base):
    codfilial = models.CharField(db_column='codfilial', unique=True, max_length=10)
    nomefilial = models.CharField(db_column='nomefilial', max_length=100, null=True)
    cnpj = models.CharField(unique=True, max_length=14)
    idempresa = models.ForeignKey(Empresa, models.CASCADE, related_name='empresas', db_column='idempresa', null=True)

    class Meta:
        managed = True
        db_table = 'filial'
        ordering = ['id']

    def __str__(self):
        return self.nomefilial

class Modulos(Base):
    modulo = models.CharField(db_column='Nomeempresa', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modulos'
        ordering = ['id']

    def __str__(self):
        return self.modulo
    
    
class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da Equipe', default=True)
    idperfil = models.IntegerField(db_column='idperfil', null=True)
    idfilial = models.ForeignKey(Filial, models.DO_NOTHING, db_column='idfilial', blank=True, null=True)
    idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='idempresa', blank=True, null=True)
    perfil = StdImageField('Imagem', upload_to='perfil', variations={'thumb': (96, 96)})
    idmodulos = models.ManyToManyField(Modulos)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email

    objects = UsuarioManager()


class File(models.Model):
    CHOICE_TIPOIMP = (
        ("CO", "CONSUMO"),
        ("RM", "RATEIO MUTAVEL"),
        ("RI", "RATEIO IMUTAVEL"),
        ("NF", "NOTA FISCAL"),
        ("CE", "CENTRO DE CUSTO"),
        ("CI", "CIRURGIA")
    ) 
    file = models.FileField(upload_to='importacao', blank=False, null=False)
    tipoimportacao = models.CharField('Tipo', max_length=2, choices=CHOICE_TIPOIMP, default='CO')

    def __str__(self):
        return self.file.name

# Create your models here.
