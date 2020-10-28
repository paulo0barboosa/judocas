from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Filiado, Professor, Academia, Pessoa
from .forms import FiliadoForm, ProfessorForm, AcademiaForm
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

@login_required
def filiados_cadastrados(request):
    filiados = Filiado.objects.all()
    return render(request, 'core/filiados_cadastrados.html', {'filiados':filiados})

# @login_required
# def cadastra_filiado(request):
#     # form_struct = FiliadoForm()
#     form = FiliadoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     return render(request, 'core/cadastra_filiado.html', {'form' : form})

@login_required
def cadastra_filiado(request):
    # academia = get_object_or_404(Academia)
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

# @login_required
class search_pessoa(ListView):
    model = Pessoa
    template_name = 'core/search_pessoa.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = ""
        object_list = Pessoa.objects.filter(
            Q(Nome__icontains=query) | Q(CPF__icontains=query)  | Q(RGNumero__icontains=query)  | Q(RegistroCBJ__icontains=query)
        )
        return object_list

class search_academia(ListView):
    model = Academia
    template_name = 'core/search_academia.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if not query :
            query = ""
        object_list = Academia.objects.filter(
            Q(Nome__icontains=query) | Q(CNPJ__icontains=query)
        )
        return object_list

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