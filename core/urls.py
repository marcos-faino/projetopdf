from django.urls import path
from .views import *

urlpatterns = [
    path('', ListarFuncionariosListView.as_view(),
         name='listar_func'),
    path('listafuncpdf/', ListaFuncPdfView.as_view(),
         name='listar_func_pdf'),
]
