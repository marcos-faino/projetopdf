from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import Funcionario
from .utils import GeraPDFMixin


class ListarFuncionariosListView(ListView):
    model = Funcionario
    template_name = 'listarfunc.html'
    context_object_name = 'funcionarios'


class ListaFuncPdfView(View, GeraPDFMixin):

    def get(self, request, *args, **kwargs):
        funcs = Funcionario.objects.all()
        contexto = {
            'funcionarios': funcs,
            'quant': funcs.count(),
        }
        # contexto['funcionarios'] = funcs
        # contexto['quant'] = funcs.count()
        return self.render_to_pdf('listarfuncpdf.html', contexto)


