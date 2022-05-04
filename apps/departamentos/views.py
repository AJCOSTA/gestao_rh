# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.departamentos.models import Departamento
from apps.funcionarios.models import Funcionario


class DepartamentoNovo(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoNovo, self).form_valid(form)


class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']


class Departamentodelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('departamentos:list_departamentos')
