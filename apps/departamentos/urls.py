from django.urls import path
from .views import DepartamentosList, DepartamentoNovo, DepartamentoEdit, Departamentodelete

# from .views import NovoClienteView, TodosClientesView, ExcluirClienteView, DetalheClienteView, EditarClienteView, \
#     IntroClienteView, GuiaClienteView
#


app_name = 'departamentos'

urlpatterns = [

    path('list', DepartamentosList.as_view(), name="list_departamentos"),
    path('novo', DepartamentoNovo.as_view(), name="create_departamentos"),
    path('editar/<int:pk>/', DepartamentoEdit.as_view(), name="update_departamentos"),
    path('deletar/<int:pk>/', Departamentodelete.as_view(), name="delete_departamentos"),


]
