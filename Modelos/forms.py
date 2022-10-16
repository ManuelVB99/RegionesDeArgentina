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

class editarblogmendoza(forms.Form):
    titulo = forms.CharField(max_length=60)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(widget= forms.Textarea(attrs={'height': '200px'}))
    autor = forms.CharField(max_length=40)
    fecha = forms.CharField(max_length=40)
    image = forms.ImageField()

class editarblogBA(forms.Form):
    titulo = forms.CharField(max_length=60)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(widget= forms.Textarea(attrs={'height': '200px'}))
    autor = forms.CharField(max_length=40)
    fecha = forms.CharField(max_length=40)
    image = forms.ImageField()

class registrousuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput())
    password2 = forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}