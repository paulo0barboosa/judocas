from django.db import models
from django.utils.timezone import now
from cpf_field.models import CPFField

# Create your models here.

class Academia(models.Model):
    Nome = models.CharField(max_length=45)
    CNPJ = models.CharField(max_length=20, unique=True)
    CEP = models.CharField(max_length=20)
    Rua = models.CharField(max_length=50)
    Numero = models.SmallIntegerField()
    Bairro = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Telefone1 = models.CharField(max_length=20)
    Telefone2 = models.CharField(max_length=20)

    def __str__(self):
        return self.Nome

class Faixa(models.Model):
    FaixaCor = models.CharField(max_length=20, default="Branca")
    # FaixaDataEntrega = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FaixaCor

class Professor(models.Model):
    # IDFiliado = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=45)
    DataNascimento = models.DateField()
    CPF = CPFField('CPF', unique=True)
    RGNumero = models.CharField(max_length=9)
    RGOrgao = models.CharField(max_length=20)
    RegistroCBJ = models.AutoField(primary_key=True, unique=True)
    Academia = models.ManyToManyField(Academia)
    Faixa = models.ForeignKey(Faixa, on_delete=models.CASCADE)
    # FaixaDataEntrega = models.DateTimeField(auto_now=True)
    CEP = models.CharField(max_length=20)
    Rua = models.CharField(max_length=50)
    Numero = models.SmallIntegerField()
    Bairro = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    # DataCadastro = models.DateField(editable=False, auto_now=True)
    Telefone1 = models.CharField(max_length=20)
    Telefone2 = models.CharField(max_length=20)
    Salario = models.DecimalField(max_digits=7,decimal_places=2)
    Observacoes = models.TextField(max_length=50)
    # UltimaAnuidade = models.DateField()

    def __str__(self):
        return self.Nome

class Filiado(models.Model):
    # IDFiliado = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=45)
    DataNascimento = models.DateField()
    CPF = CPFField('CPF', unique=True)
    RGNumero = models.CharField(max_length=9)
    RGOrgao = models.CharField(max_length=20)
    RegistroCBJ = models.AutoField(primary_key=True, unique=True)
    Academia = models.ForeignKey(Academia, on_delete=models.CASCADE)
    Professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    Faixa = models.ForeignKey(Faixa, on_delete=models.CASCADE)
    FaixaDataEntrega = models.DateTimeField(auto_now=True)
    CEP = models.CharField(max_length=20)
    Rua = models.CharField(max_length=50)
    Numero = models.SmallIntegerField()
    Bairro = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Telefone1 = models.CharField(max_length=20)
    Telefone2 = models.CharField(max_length=20)
    Observacoes = models.TextField(max_length=50)
    UltimaAnuidade = models.DateField()
    DataCadastro = models.DateField(editable=False, auto_now=True)

    def __str__(self):
        return self.Nome
