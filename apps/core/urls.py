from django.urls import path
from .views import home

# from .views import NovoClienteView, TodosClientesView, ExcluirClienteView, DetalheClienteView, EditarClienteView, \
#     IntroClienteView, GuiaClienteView
#


app_name = 'core'

urlpatterns = [

    path('', home, name="core_home"),

]
