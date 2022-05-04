# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.departamentos.models import Departamento
from apps.documentos.models import Documento
from apps.funcionarios.models import Funcionario


class DocumentoNovo(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('funcionarios:update_funcionario', args=[self.kwargs['funcionario_id']])
