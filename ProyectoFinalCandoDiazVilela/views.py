from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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