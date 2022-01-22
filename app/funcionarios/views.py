from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    # Trazer somente funcionario da empresa logada
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
