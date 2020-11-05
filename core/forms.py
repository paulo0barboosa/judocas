from django import forms
from django.forms import ModelForm
from localflavor.br.forms import BRZipCodeField, BRCNPJField
from .models import Filiado, Professor, Academia

# class DateInput(forms.DateInput):
#     input_type = 'date'

class FiliadoForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    # Estado = BRStateChoiceField(label='Estado')

    # def __init__(self,*args,**kwargs):
    #     super (FiliadoForm,self ).__init__(*args,**kwargs) # populates the post
    #     # self.fields['Academia'].queryset = Filiado.objects.filter(Academia=Academia)
    #     self.fields['Professor'].queryset = Professor.objects.filter(Academia=Academia)

    class Meta:
        model = Filiado
        fields = '__all__'
        # widgets = {
        #     'DataNascimento': DateInput(),
        #     'UltimaAnuidade': DateInput()
        # }

class ProfessorForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    # Estado = BRStateChoiceField(label='Estado')

    class Meta:
        model = Professor
        fields = '__all__'
        # widgets = {
        #     'DataNascimento': DateInput()
        # }

class AcademiaForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    # Estado = BRStateChoiceField(label='Estado')
    CNPJ = BRCNPJField(label='CNPJ')

    class Meta:
        model = Academia
        fields = '__all__'