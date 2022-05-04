from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView

from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)