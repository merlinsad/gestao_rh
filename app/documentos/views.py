from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView

from app.documentos.models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    # Linkar funcionario com Empresa
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('update_funcionarios', args=[self.kwargs['funcionario_id']])


class DocumentoEdit:
    pass


class DocumentoDelete(DeleteView):
    model = Documento
    fields = ['descricao', 'arquivo']
    success_url = reverse_lazy('list_funcionarios')