from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from Modelos.forms import registrousuario, AvatarFormulario, UserEditForm, ChangePasswordForm
from Modelos.models import Avatar

def index(request):
    return render(request, 'index.html')

def error404(request, exception):
    return render(request, "error404.html")

def aboutus(request):
    return render(request, "aboutus.html")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username=user, password=pwd)

            if user is not None:
                login(request, user)

                return render(request, 'index.html')
                
            else:
                return render(request, "login.html", {'form': form})
        else:
            return render(request, "login.html", {'form': form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro(request):
    form = registrousuario(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/login/")
        else:
            return render(request, "registro.html", {'form': form})

    form = registrousuario()
    return render(request, "registro.html", {'form': form})


@login_required
def editarperfil(request):
    usuario = request.user
    user_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_info.username = form.cleaned_data.get('username')
            user_info.email = form.cleaned_data.get('email')
            user_info.first_name = form.cleaned_data.get('first_name')
            user_info.last_name = form.cleaned_data.get('last_name')
            user_info.save()
            avatar = Avatar.objects.filter(user=request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'perfil.html', {"avatar": avatar})
            
        else:
            return render(request, "index.html", {'form': form})
    else:
        form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
    return render(request, "editarperfil.html", {'form': form, 'usuario': usuario})

@login_required
def cambiarpassword(request):
    usuario = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'index.html')
            
    else:
        form = ChangePasswordForm(data = request.POST, user = usuario)
    return render(request, 'cambiarpassword.html', {'form': form, 'usuario': usuario})

@login_required
def perfilView(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'perfil.html', {"avatar": avatar})

@login_required
def agregaravatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id= request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user=request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'perfil.html', {"avatar": avatar})
            
    else:
        form = AvatarFormulario()
    return render(request, 'agregaravatar.html', {'form': form})



