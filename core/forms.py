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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Professor'].queryset = Professor.objects.none()

        if 'Academia' in self.data:
            try:
                Academia_id = int(self.data.get('Academia'))
                self.fields['Professor'].queryset = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.RegistroCBJ:
        #     self.fields['Professor'].queryset = self.instance.Academia.Professor_set.order_by('Nome')

class UpdateFiliadoForm(ModelForm):
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['Professor'].queryset = self.data.get('Professor')

        if 'Academia' in self.data:
            try:
                Academia_id = int(self.data.get('Academia'))
                self.fields['Professor'].queryset = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.RegistroCBJ:
        #     self.fields['Professor'].queryset = self.instance.Academia.Professor_set.order_by('Nome')

class ProfessorForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    # Estado = BRStateChoiceField(label='Estado')

    class Meta:
        model = Professor
        fields = '__all__'
        # widgets = {
        #     'DataNascimento': DateInput()
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Professor'].queryset = Professor.objects.none()

        if 'Academia' in self.data:
            try:
                Academia_id = int(self.data.get('Academia'))
                self.fields['Professor'].queryset = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.RegistroCBJ:
        #     self.fields['Professor'].queryset = self.instance.Academia.Professor_set.order_by('Nome')

class AcademiaForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    # Estado = BRStateChoiceField(label='Estado')
    CNPJ = BRCNPJField(label='CNPJ')

    class Meta:
        model = Academia
        fields = '__all__'

class UpdateProfessorForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    # Estado = BRStateChoiceField(label='Estado')

    class Meta:
        model = Professor
        fields = '__all__'
        # widgets = {
        #     'DataNascimento': DateInput()
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['Professor'].queryset = Professor.objects.none()

        if 'Academia' in self.data:
            try:
                Academia_id = int(self.data.get('Academia'))
                self.fields['Professor'].queryset = Professor.objects.filter(Academia_id=Academia_id).order_by('Nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.RegistroCBJ:
        #     self.fields['Professor'].queryset = self.instance.Academia.Professor_set.order_by('Nome')

class AcademiaForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    # Estado = BRStateChoiceField(label='Estado')
    CNPJ = BRCNPJField(label='CNPJ')

    class Meta:
        model = Academia
        fields = '__all__'