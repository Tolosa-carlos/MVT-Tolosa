from django.http import HttpResponse
from mvt_app.models import *

# Create your views here.

def lista_familia(request):
    lista = datos_fam.objects.all()

    vista = []
    for familia in lista:

        vista += f"{familia.nombre}, {familia.edad}, {familia.nacimiento}" + " - "

    return HttpResponse(vista)