from django.shortcuts import render
from Modelos.models import *

def noroeste(request):
    return render(request, "Noroeste/noroeste.html")

def blogssalta(request):
    blogsalta = BlogsSalta.objects.all()
    return render(request, "Noroeste/salta.html", {"blogsalta" : blogsalta})

def agregarblog(request):
    if request.method == 'POST':
        nuevoblog = BlogsSalta(titulo = request.POST['titulo'], subtitulo = request.POST['subtitulo'], cuerpo = request.POST['cuerpo'], autor = request.POST["autor"], fecha = request.POST["fecha"], image = request.FILES["image"])
        nuevoblog.save()
        blogsalta = BlogsSalta.objects.all()
        return render(request, "Noroeste/salta.html", {"blogsalta": blogsalta})
    return render(request, "Noroeste/crud_salta/agregarblog.html")



# Create your views here.
