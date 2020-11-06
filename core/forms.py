from django import forms
from django.forms import ModelForm
from localflavor.br.forms import BRZipCodeField, BRCNPJField
from .models import Filiado, Professor, Academia

class FiliadoForm(ModelForm): # funcao para cadastrar um filiado
    CEP = BRZipCodeField(label='CEP') # aplica a validacao de CEP

    class Meta:
        model = Filiado # seleciona a classe filiado
        fields = '__all__' # seleciona todos os atributos disponiveis
    
    def __init__(self, *args, **kwargs): # ao inicializar o formulario, realiza a funcao abaixo
        super().__init__(*args, **kwargs) # varre todos os campos
        self.fields['Professor'].queryset = Professor.objects.none() # seleciona o campo professor e retira todos os objetos dele, para limpar o filtro quando a pagina for carregada

        if 'Academia' in self.data: # se localizar o campo academia
            try:
                Academia_id = int(self.data.get('Academia')) # ele pega academia selecinada
                self.fields['Professor'].queryset = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome') # e filtra os professores que trabalham nessa academia
            except (ValueError, TypeError): # se der errado, ignora a funcao para que nao retorne nenhum erro
                pass

class UpdateFiliadoForm(ModelForm):  # funcao para atualizar um filiado
    CEP = BRZipCodeField(label='CEP') # aplica a validacao de CEP

    class Meta:
        model = Filiado # seleciona a classe filiado
        fields = '__all__' # seleciona todos os atributos disponiveis
    
    def __init__(self, *args, **kwargs): # a diferenca e que agora os objetos do campo professor nao serao removidos
        super().__init__(*args, **kwargs)

        if 'Academia' in self.data:
            try:
                Academia_id = int(self.data.get('Academia'))
                self.fields['Professor'].queryset = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome')
            except (ValueError, TypeError):
                pass

class ProfessorForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')

    class Meta:
        model = Professor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Professor'].queryset = Professor.objects.none()

        if 'Academia' in self.data:
            try:
                Academia_id = int(self.data.get('Academia'))
                self.fields['Professor'].queryset = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome')
            except (ValueError, TypeError):
                pass 

class UpdateProfessorForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')

    class Meta:
        model = Professor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'Academia' in self.data:
            try:
                Academia_id = int(self.data.get('Academia'))
                self.fields['Professor'].queryset = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome')
            except (ValueError, TypeError):
                pass

class AcademiaForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    CNPJ = BRCNPJField(label='CNPJ')

    class Meta:
        model = Academia
        fields = '__all__'