from django.shortcuts import render
from Modelos.models import *
from Modelos.forms import *

def noroeste(request):
    return render(request, "Noroeste/noroeste.html")

def patagonia(request):
    return render(request, "Patagonia/patagonia.html")    

def blogssalta(request):
    blogsalta = BlogsSalta.objects.all()
    return render(request, "Noroeste/salta.html", {"blogsalta" : blogsalta})

def blogsrionegro(request):
    blogrionegro = BlogsRioNegro.objects.all()
    return render(request, "Patagonia/rionegro.html", {"blogrionegro" : blogrionegro})

def leerblogSalta(request, blogsalta_id):
    blog = BlogsSalta.objects.get(id = blogsalta_id)
    img = blog.image
    return render(request, "Noroeste/crud_salta/leerblogSalta.html", {"blog": blog, "img": img})

def leerblogRioNegro(request, blogrionegro_id):
    blog = BlogsRioNegro.objects.get(id = blogrionegro_id)
    img = blog.image
    return render(request, "Patagonia/crud_rionegro/leerblogRioNegro.html", {"blog": blog, "img": img})

def agregarblogSalta(request):
    if request.method == 'POST':
        nuevoblog = BlogsSalta(titulo = request.POST['titulo'], subtitulo = request.POST['subtitulo'], cuerpo = request.POST['cuerpo'], autor = request.POST["autor"], fecha = request.POST["fecha"], image = request.FILES["image"])
        nuevoblog.save()
        blogsalta = BlogsSalta.objects.all()
        return render(request, "Noroeste/salta.html", {"blogsalta": blogsalta})
    return render(request, "Noroeste/crud_salta/agregarblogSalta.html")

def agregarblogRioNegro(request):
    if request.method == 'POST':
        nuevoblog = BlogsRioNegro(titulo = request.POST['titulo'], subtitulo = request.POST['subtitulo'], cuerpo = request.POST['cuerpo'], autor = request.POST["autor"], fecha = request.POST["fecha"], image = request.FILES["image"])
        nuevoblog.save()
        blogrionegro = BlogsRioNegro.objects.all()
        return render(request, "Patagonia/rionegro.html", {"blogrionegro": blogrionegro})
    return render(request, "Patagonia/crud_rionegro/agregarblogRioNegro.html")

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

def editarblogRioNegro(request, blogrionegro_id):
    blog = BlogsRioNegro.objects.get(id = blogrionegro_id)

    if request.method == 'POST':
        formulario = editarblogrionegro(request.POST, request.FILES)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            blog.titulo = informacion['titulo']
            blog.subtitulo = informacion['subtitulo']
            blog.cuerpo = informacion['cuerpo']
            blog.autor = informacion["autor"]
            blog.fecha = informacion["fecha"]
            blog.image = informacion["image"]
            blog.save()
            blogrionegro = BlogsRioNegro.objects.all()
            return render(request, "Patagonia/rionegro.html", {"blogrionegro": blogrionegro})
    else:
        formulario = editarblogrionegro(initial={'titulo': blog.titulo, 'subtitulo': blog.subtitulo, 'cuerpo': blog.cuerpo, "autor": blog.autor, "fecha": blog.fecha, "image": None})
    return render(request, "Patagonia/crud_rionegro/editarblogRioNegro.html", {"formulario": formulario})

def borrarblogSalta(request, blogsalta_id):
    blog = BlogsSalta.objects.get(id = blogsalta_id)
    blog.delete()

    blogsalta = BlogsSalta.objects.all()
    return render(request, "Noroeste/salta.html", {"blogsalta": blogsalta})

def borrarblogRioNegro(request, blogrionegro_id):
    blog = BlogsRioNegro.objects.get(id = blogrionegro_id)
    blog.delete()

    blogrionegro = BlogsRioNegro.objects.all()
    return render(request, "Patagonia/rionegro.html", {"blogrionegro": blogrionegro})
# Create your views here.
