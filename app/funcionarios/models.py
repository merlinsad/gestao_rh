from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from app.departamentos.models import Departamento
from app.empresas.models import Empresa

# OneToOneField = Um usuário só pode ter um funcionario(Linha 12)
# ManyToManyField = Um departamento pode ter vários funcionários(13)


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa,
                                on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome

