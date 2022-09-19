from django.db import models

class Familia(models.Model):

    nombre=models.CharField(max_length=60)
    edad=models.IntegerField(max_length=99)
    dni=models.IntegerField(max_length=9)