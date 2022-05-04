from django.urls import path
from .views import EmpresaCreate, EmpresaEdit

# from .views import NovoClienteView, TodosClientesView, ExcluirClienteView, DetalheClienteView, EditarClienteView, \
#     IntroClienteView, GuiaClienteView
#


app_name = 'empresas'

urlpatterns = [

    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),

]
