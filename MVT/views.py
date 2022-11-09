from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def fecha(request):
    fecha_actual = datetime.now().strftime("%y-%m-%d")

    return HttpResponse(f"{fecha_actual}")

def datos_familia(request):

    archivo = open(r"C:\Users\carlo_cq0emdi\OneDrive\Escritorio\MVT_Tolosa\MVT\MVT\plantillas\vista.html")

    plantilla = Template(archivo.read())
    archivo.close()

    fecha_actual = datetime.now()

    nombre = ["Ingrid Tolosa", "Rodrigo Tolosa", "Astrid Fernandez"]

    edad = [21, 25, 55]

    fecha_nac = ["2001-06-07", "1996-09-16", "1965-02-17"]

    datos = {"Nombre": nombre, "Edad": edad, "Fecha_Nacimiento": fecha_nac, "Fecha": fecha_actual}

    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)