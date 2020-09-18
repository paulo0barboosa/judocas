from django.db import models
from django.utils.timezone import now

# Create your models here.

class Filiado(models.Model):
    IDFiliado = models.AutoField(primary_key=True)
    RegistroCBJ = models.CharField(max_length=20, default="")
    Nome = models.CharField(max_length=45)
    CPF = models.CharField(max_length=11)
    Categoria = models.CharField(max_length=20, default="")
    RGNumero = models.CharField(max_length=9)
    RGOrgao = models.CharField(max_length=20, default="")
    FaixaCor = models.CharField(max_length=20, default="Branco")
    FaixaDataEntrega = models.DateField(default=now)
    # EnderecoID = models.IntegerField()
    DataNascimento = models.DateField(default=now)
    DataCadastro = models.DateField(editable=False, default=now)
    Telefone1 = models.CharField(max_length=20, default="")
    Telefone2 = models.CharField(max_length=20, default="")
    Observacoes = models.TextField(max_length=50, default="")
    UltimaAnuidade = models.DateField(default=now)

    def __str__(self):
        return self.Nome