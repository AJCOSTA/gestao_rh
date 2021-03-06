from django.urls import path
from .views import HoraExtraList, HoraExtraEdit, FuncionarioDelete, HoraExtraNovo

# from .views import NovoClienteView, TodosClientesView, ExcluirClienteView, DetalheClienteView, EditarClienteView, \
#     IntroClienteView, GuiaClienteView
#


app_name = 'hora_extra'

urlpatterns = [

    path('', HoraExtraList.as_view(), name="list_hora_extra"),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name="update_hora_extra"),
    path('novo/', HoraExtraNovo.as_view(), name="create_hora_extra"),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name="delete_hora_extra"),

]
