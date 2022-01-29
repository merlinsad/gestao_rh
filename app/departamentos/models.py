from django.db import models
from django.urls import reverse

from app.empresas.models import Empresa


# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do departamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('list_departamentos')

    def __str__(self):
        return self.nome