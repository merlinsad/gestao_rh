from django.db import models
from app.funcionarios.models import Funcionario


# ForeignKey = Um funcionario pode ter vários documentos
# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Nome do documento')
    pertence = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao