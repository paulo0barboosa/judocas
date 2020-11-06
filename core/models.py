from django.db import models
from django.utils.timezone import now
from cpf_field.models import CPFField

# Create your models here.
class Academia(models.Model): # Classe Academia
    IDAcademia = models.AutoField(primary_key=True, unique=True)
    Nome = models.CharField(max_length=45)
    CNPJ = models.CharField(max_length=20, unique=True)
    CEP = models.CharField(max_length=20)
    Rua = models.CharField(max_length=50)
    Numero = models.SmallIntegerField()
    Complemento = models.CharField(max_length=50, blank=True, null=True)
    Bairro = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Telefone1 = models.CharField(max_length=20)
    Telefone2 = models.CharField(max_length=20)

    def __str__(self):
        return self.Nome

class Faixa(models.Model): # Classe Faixa
    FaixaCor = models.CharField(max_length=20, default="Branca")

    def __str__(self):
        return self.FaixaCor

        
class Pessoa(models.Model): # Classe Pessoa
    Nome = models.CharField(max_length=45)
    DataNascimento = models.DateField()
    CPF = CPFField('CPF', unique=True)
    RGNumero = models.CharField(max_length=12, unique=True)
    RGOrgao = models.CharField(max_length=20)
    RegistroCBJ = models.AutoField(primary_key=True, unique=True, editable=False)
    Faixa = models.ForeignKey(Faixa, on_delete=models.CASCADE)
    FaixaDataEntrega = models.DateTimeField(auto_now=True)
    CEP = models.CharField(max_length=20)
    Rua = models.CharField(max_length=50)
    Numero = models.SmallIntegerField()
    Complemento = models.CharField(max_length=50, blank=True, null=True)
    Bairro = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Telefone1 = models.CharField(max_length=20)
    Telefone2 = models.CharField(max_length=20)
    Observacoes = models.TextField(max_length=50, blank=True, null=True)
    DataCadastro = models.DateField(editable=False, auto_now=True)

class Professor(Pessoa): # Classe Professor, herda Pessoa
    Academia = models.ForeignKey(Academia, on_delete=models.CASCADE)
    Salario = models.DecimalField(max_digits=7,decimal_places=2)
    ProfessorAluno = models.BooleanField(default=False)
    Professor = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    UltimaAnuidade = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Nome

class Filiado(Pessoa): # Classe Filiado (Aluno), herda Pessoa
    Academia = models.ForeignKey(Academia, on_delete=models.CASCADE)
    Professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    UltimaAnuidade = models.DateField()

    def __str__(self):
        return self.Nome
