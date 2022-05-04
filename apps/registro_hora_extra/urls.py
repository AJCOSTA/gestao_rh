from django.urls import path
from .views import HoraExtraList
# from .views import NovoClienteView, TodosClientesView, ExcluirClienteView, DetalheClienteView, EditarClienteView, \
#     IntroClienteView, GuiaClienteView
#


app_name = 'hora_extra'

urlpatterns = [

    path('', HoraExtraList.as_view(), name="list_hora_extra"),
    # path('editar/<int:pk>/', FuncionarioEdit.as_view(), name="update_funcionario"),
    # path('novo/', FuncionarioNovo.as_view(), name="create_funcionario"),
    # path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name="delete_funcionario"),

]
