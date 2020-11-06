from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Filiado, Professor, Academia, Pessoa
from .forms import FiliadoForm, UpdateFiliadoForm, ProfessorForm, UpdateProfessorForm, AcademiaForm


def home(request): # pagina inicial
    return render(request, 'core/index.html')

# -------------- CADASTRO --------------
@login_required # esta marcacao indica que a funcao so sera executada se o usuario estiver logado
def cadastra_filiado(request):
    form = FiliadoForm(request.POST or None) # pega a funcao de formulario do forms.py
    if form.is_valid(): # valida o formulario
        form.save() # se estiver tudo certo, ele salva os dados do formulario no banco de dados
        return redirect("core_cadastra_filiado") # da um refresh na pagina
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

def load_professores(request): #funcao para carregar os professores que trabalham na academia selecionada
    Academia_id = request.GET.get('Academia')
    professores = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome')
    return render(request, 'core/professor_dropdown_list.html', {'professores': professores})

# -------------- BUSCA --------------
class search_pessoa(ListView):
    model = Pessoa
    template_name = 'core/search_pessoa.html'

    def get_queryset(self): # funcao para aplicar os filtros de busca
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

    try: # se o RegistroCBJ estiver presente dentro da classe filiado, o request e de um filiado
        pessoa = Filiado.objects.get(RegistroCBJ=RegistroCBJ)
        form = UpdateFiliadoForm(request.POST or None, instance=pessoa)
    except Filiado.DoesNotExist: # caso contrario e um professor
        pessoa = Professor.objects.get(RegistroCBJ=RegistroCBJ)   
        form = UpdateProfessorForm(request.POST or None, instance=pessoa)

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