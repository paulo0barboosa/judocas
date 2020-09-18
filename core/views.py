from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Filiado
from .forms import FiliadoForm
# Create your views here.


def home(request):
    return render(request, 'core/index.html')

def filiados_cadastrados(request):
    filiados = Filiado.objects.all()
    return render(request, 'core/filiados_cadastrados.html', {'filiados':filiados})

def cadastra_filiado(request):
    # form_struct = FiliadoForm()
    form = FiliadoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'core/cadastro.html', {'form' : form})