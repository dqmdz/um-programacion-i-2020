from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
# pone como parametro el modelo question
# y me permite agregar preguntas en la 
# base de datos
