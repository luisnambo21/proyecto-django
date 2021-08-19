from django import forms
from .models import ComentarioForm
from .models import ComentarioCurso
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

class ComentarioFormulario(forms.ModelForm):
    class Meta: 
        model = ComentarioForm
        fields = ['nombre','correo','curso','mensaje']

class ComentarioFormCurso(forms.ModelForm):
    class Meta: 
        model = ComentarioCurso
        fields = ['mat','tur','matricula','calif']

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ('titulo', 'archivo')
        widgets = {
            'archivo': CustomClearableFileInput
        }