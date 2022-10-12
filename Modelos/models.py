from django.db import models

class BlogsSalta(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    image = models.ImageField(upload_to='blogsalta', null = True, blank = True)

class BlogsRioNegro(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    autor = models.CharField(max_length=40)
    fecha = models.CharField(max_length=40)
    image = models.ImageField(upload_to='blogrionegro', null = True, blank = True)

# Create your models here.
