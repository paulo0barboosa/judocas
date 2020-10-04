from django.forms import ModelForm
from localflavor.br.forms import BRZipCodeField, BRStateChoiceField, BRCNPJField
from .models import Filiado, Professor, Academia

class FiliadoForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    Estado = BRStateChoiceField(label='Estado')

    class Meta:
        model = Filiado
        fields = '__all__'

class ProfessorForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    Estado = BRStateChoiceField(label='Estado')

    class Meta:
        model = Professor
        fields = '__all__'

class AcademiaForm(ModelForm):
    CEP = BRZipCodeField(label='CEP')
    Estado = BRStateChoiceField(label='Estado')
    CNPJ = BRCNPJField(label='CNPJ')

    class Meta:
        model = Academia
        fields = '__all__'