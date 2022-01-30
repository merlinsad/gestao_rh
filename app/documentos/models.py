from django.db import models
from django.urls import reverse

from app.funcionarios.models import Funcionario


# ForeignKey = Um funcionario pode ter vários documentos
# FileField = Função para campo de arquivos
# Create your models here.
class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.pertence.id])

    def __str__(self):
        return self.descricao

