from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Filiado, Professor, Academia
from .forms import FiliadoForm, ProfessorForm, AcademiaForm
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

@login_required
def filiados_cadastrados(request):
    filiados = Filiado.objects.all()
    return render(request, 'core/filiados_cadastrados.html', {'filiados':filiados})

@login_required
def cadastra_filiado(request):
    # form_struct = FiliadoForm()
    form = FiliadoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'core/cadastra_filiado.html', {'form' : form})

@login_required
def cadastra_professor(request):
    # form_struct = FiliadoForm()
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'core/cadastra_professor.html', {'form' : form})

@login_required
def professores_cadastrados(request):
    professores = Professor.objects.all()
    return render(request, 'core/professores_cadastrados.html', {'professores':professores})

@login_required
def cadastra_academia(request):
    # form_struct = FiliadoForm()
    form = AcademiaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'core/cadastra_academia.html', {'form' : form})

@login_required
def academias_cadastrados(request):
    academias = Academia.objects.all()
    return render(request, 'core/academias_cadastrados.html', {'academias':academias})