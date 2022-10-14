from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def error404(request, exception):
    return render(request, "error404.html")

def aboutus(request):
    return render(request, "aboutus.html")