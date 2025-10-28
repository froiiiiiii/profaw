from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pais, Estudiante

admin.site.register(Pais)
admin.site.register(Estudiante)
