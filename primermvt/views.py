from fileinput import close
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from primermvt.models import Familia
from django.template import Template, Context



def familia(self):

    padre = Familia(nombre="Juan", edad=68, dni=10090875)
    padre.save()
    madre = Familia(nombre="Maria", edad=66, dni=12265987)
    madre.save()
    hijo = Familia(nombre="Luis", edad=42, dni=27487279)
    hijo.save()


    diccionario = "nombre", {padre.nombre}, "edad", {padre.edad}, "años",  "dni:", {padre.dni}, "2° integrante de mi familia", {madre.nombre}, "edad", {madre.edad}, "años"   "dni:", {madre.dni}, "3° integrante de mi familia ",{hijo.nombre}, "edad", {hijo.edad}, "años"  "dni:", {hijo.dni}
    miHtml = open("C:/Users/Parra/Desktop/NUESTRO PRIMER MVT/PRIMERMVT/PRIMERMVT/plantillas/plantilla.html")
    plantilla = Template(miHtml.read())
    miHtml.close
    miContexto = Context()
    documento = plantilla.render(miContexto)
    plantilla=loader.get_template("plantilla.html")
    return HttpResponse(diccionario)