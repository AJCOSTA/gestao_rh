from django.db import models
from django.shortcuts import redirect


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')

    def __str__(self):

        if self.nome:
            return f'{self.id} - {self.nome}'
        else:
            return f'{self.id}'

    def get_absolute_url(self):
        return redirect('core:core_home')
