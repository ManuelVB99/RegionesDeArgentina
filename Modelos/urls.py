from django.urls import path
from Modelos.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("noroeste/", noroeste),
    path("noroeste/salta/", blogssalta),
    path("noroeste/salta/agregarblog/", agregarblog)


]