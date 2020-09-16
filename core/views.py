from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Filiado
from .forms import FiliadoForm
# Create your views here.


def home(request):
    context = {'mensagem' : 'corno'}
    return render(request, 'core/index.html', context)

def filiados_cadastrados(request):
    filiados = Filiado.objects.all()
    form = FiliadoForm()
    data =  {'filiados':filiados, 'form':form}
    return render(request, 'core/filiados_cadastrados.html', data)

def cadastra_filiado(request):
    form = FiliadoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_filiados_cadastrados')