from django.shortcuts import render
from Modelos.models import *
from Modelos.forms import *

def noroeste(request):
    return render(request, "Noroeste/noroeste.html")

def blogssalta(request):
    blogsalta = BlogsSalta.objects.all()
    return render(request, "Noroeste/salta.html", {"blogsalta" : blogsalta})

def leerblogSalta(request, blogsalta_id):
    blog = BlogsSalta.objects.get(id = blogsalta_id)
    img = blog.image
    return render(request, "Noroeste/crud_salta/leerblogSalta.html", {"blog": blog, "img": img})

def agregarblogSalta(request):
    if request.method == 'POST':
        nuevoblog = BlogsSalta(titulo = request.POST['titulo'], subtitulo = request.POST['subtitulo'], cuerpo = request.POST['cuerpo'], autor = request.POST["autor"], fecha = request.POST["fecha"], image = request.FILES["image"])
        nuevoblog.save()
        blogsalta = BlogsSalta.objects.all()
        return render(request, "Noroeste/salta.html", {"blogsalta": blogsalta})
    return render(request, "Noroeste/crud_salta/agregarblogSalta.html")

def editarblogSalta(request, blogsalta_id):
    blog = BlogsSalta.objects.get(id = blogsalta_id)

    if request.method == 'POST':
        formulario = editarblogsalta(request.POST, request.FILES)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            blog.titulo = informacion['titulo']
            blog.subtitulo = informacion['subtitulo']
            blog.cuerpo = informacion['cuerpo']
            blog.autor = informacion["autor"]
            blog.fecha = informacion["fecha"]
            blog.image = informacion["image"]
            blog.save()
            blogsalta = BlogsSalta.objects.all()
            return render(request, "Noroeste/salta.html", {"blogsalta": blogsalta})
    else:
        formulario = editarblogsalta(initial={'titulo': blog.titulo, 'subtitulo': blog.subtitulo, 'cuerpo': blog.cuerpo, "autor": blog.autor, "fecha": blog.fecha, "image": None})
    return render(request, "Noroeste/crud_salta/editarblogSalta.html", {"formulario": formulario})

def borrarblogSalta(request, blogsalta_id):
    blog = BlogsSalta.objects.get(id = blogsalta_id)
    blog.delete()

    blogsalta = BlogsSalta.objects.all()
    return render(request, "Noroeste/salta.html", {"blogsalta": blogsalta})
# Create your views here.
