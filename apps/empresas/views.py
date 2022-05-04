from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
from apps.empresas.models import Empresa


class EmpresaCreate(CreateView, SuccessMessageMixin):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse("ok")


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']

    success_url = reverse_lazy('core:core_home')
    success_message = "Empresa %(nome)s Editado com Sucesso"
