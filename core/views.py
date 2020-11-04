from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Filiado, Professor, Academia, Pessoa
from .forms import FiliadoForm, ProfessorForm, AcademiaForm


def home(request):
    return render(request, 'core/index.html')


# -------------- CADASTRO --------------
@login_required
def cadastra_filiado(request):
    form = FiliadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("core_cadastra_filiado")
    return render(request, 'core/cadastra_filiado.html', {'form' : form})

@login_required
def cadastra_professor(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("core_cadastra_professor")
    return render(request, 'core/cadastra_professor.html', {'form' : form})

@login_required
def cadastra_academia(request):
    form = AcademiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("core_cadastra_academia")
    return render(request, 'core/cadastra_academia.html', {'form' : form})


# -------------- BUSCA --------------
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


# -------------- UPDATE --------------
@login_required
def update_pessoa(request, RegistroCBJ):
    data = {}

    try:
        pessoa = Filiado.objects.get(RegistroCBJ=RegistroCBJ)
        form = FiliadoForm(request.POST or None, instance=pessoa)
    except Filiado.DoesNotExist:
        pessoa = Professor.objects.get(RegistroCBJ=RegistroCBJ)   
        form = ProfessorForm(request.POST or None, instance=pessoa)

    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("search_pessoa")
    # else:
    return render(request, 'core/update_pessoa.html', data)

@login_required
def update_academia(request, IDAcademia):
    data = {}
    academia = Academia.objects.get(IDAcademia=IDAcademia)
    form = AcademiaForm(request.POST or None, instance=academia)
    data['academia'] = academia
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("search_academia")
    # else:
    return render(request, 'core/update_academia.html', data)


# -------------- DELETE --------------
@login_required
def delete_pessoa(request, RegistroCBJ):
    try:
        pessoa = Filiado.objects.get(RegistroCBJ=RegistroCBJ)
    except Filiado.DoesNotExist:
        pessoa = Professor.objects.get(RegistroCBJ=RegistroCBJ)   

    if request.method == 'POST':
        pessoa.delete()
        return redirect("search_pessoa")
    # else:
    return render(request, 'core/delete_pessoa.html', {'pessoa': pessoa})

@login_required
def delete_academia(request, IDAcademia):
    academia = Academia.objects.get(IDAcademia=IDAcademia)

    if request.method == 'POST':
        academia.delete()
        return redirect("search_academia")
    # else:
    return render(request, 'core/delete_academia.html', {'academia': academia})


# -------------- LISTAGEM --------------

# @login_required
# def filiados_cadastrados(request):
#     filiados = Filiado.objects.all()
#     return render(request, 'core/filiados_cadastrados.html', {'filiados':filiados})

# @login_required
# def professores_cadastrados(request):
#     professores = Professor.objects.all()
#     return render(request, 'core/professores_cadastrados.html', {'professores':professores})

# @login_required
# def academias_cadastrados(request):
#     academias = Academia.objects.all()
#     return render(request, 'core/academias_cadastrados.html', {'academias':academias})