from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class editarblogsalta(forms.Form):
    titulo = forms.CharField(max_length=60)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(widget= forms.Textarea(attrs={'height': '200px'}))
    autor = forms.CharField(max_length=40)
    fecha = forms.CharField(max_length=40)
    image = forms.ImageField()

class editarblogrionegro(forms.Form):
    titulo = forms.CharField(max_length=60)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(widget= forms.Textarea(attrs={'height': '200px'}))
    autor = forms.CharField(max_length=40)
    fecha = forms.CharField(max_length=40)
    image = forms.ImageField()