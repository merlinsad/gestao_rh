from django.db import models
from app.funcionarios.models import Funcionario


# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Nome do documento')
    pertence = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao