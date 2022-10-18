from django.urls import path
from Modelos.views import *

urlpatterns = [
    path("noroeste/", noroeste),
    path("noroeste/salta/", blogssalta),
    path("noroeste/salta/agregarblogSalta/", agregarblogSalta),
    path('noroeste/salta/editarblogSalta/<blogsalta_id>', editarblogSalta),
    path("noroeste/salta/borrarblogSalta/<blogsalta_id>", borrarblogSalta),
    path("noroeste/salta/leerblogSalta/<blogsalta_id>", leerblogSalta),

    path("patagonia/", patagonia),
    path("patagonia/rionegro/", blogsrionegro),
    path("patagonia/rionegro/agregarblogRioNegro/", agregarblogRioNegro),
    path('patagonia/rionegro/editarblogRioNegro/<blogrionegro_id>', editarblogRioNegro),
    path("patagonia/rionegro/borrarblogRioNegro/<blogrionegro_id>", borrarblogRioNegro),
    path("patagonia/rionegro/leerblogRioNegro/<blogrionegro_id>", leerblogRioNegro),

    path("cuyo/", cuyo),
    path("cuyo/mendoza/", blogsmendoza),
    path("cuyo/mendoza/agregarblogMendoza/", agregarblogMendoza),
    path('cuyo/mendoza/editarblogMendoza/<blogmendoza_id>', editarblogMendoza),
    path("cuyo/mendoza/borrarblogMendoza/<blogmendoza_id>", borrarblogMendoza),
    path("cuyo/mendoza/leerblogMendoza/<blogmendoza_id>", leerblogMendoza),

    path("pampeana/", pampeana),
    path("pampeana/buenosaires/", blogsbuenosaires),
    path("pampeana/buenosaires/agregarblogBA/", agregarblogBA),
    path("pampeana/buenosaires/leerblogBA/<blogBA_id>/", leerblogBA),
    path("pampeana/buenosaires/borrarblogBA/<blogBA_id>/", borrarblogBA),
    path("pampeana/buenosaires/editarblogsBA/<blogBA_id>/", editarblogsBA),


]