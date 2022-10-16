from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from Modelos.forms import registrousuario
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

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
            return render(request, "editarperfil.html")
        else:
            return render(request, "index.html", {'form': form})
    else:
        form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
    return render(request, "editarperfil.html", {'form': form, 'usuario': usuario})