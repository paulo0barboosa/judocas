from django.db import models

# Create your models here.

class Filiado(models.Model):
    ID_Filiado = models.IntegerField()
    Nome = models.CharField(max_length=45)
    CPF = models.CharField(max_length=11)

    def __str__(self):
        return self.Nome