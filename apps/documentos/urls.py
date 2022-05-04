from django.urls import path
from .views import DocumentoNovo

app_name = 'documentos'

urlpatterns = [

    path('novo/<int:funcionario_id>/', DocumentoNovo.as_view(), name="create_documento"),
    #
    # path('deletar/<int:pk>/', Documentodelete.as_view(), name="delete_documentos"),

]
