from django.forms import ModelForm
from .models import Filiado

class FiliadoForm(ModelForm):
    class Meta:
        model = Filiado
        fields = '__all__'