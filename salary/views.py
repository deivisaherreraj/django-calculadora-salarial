from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

# Instanciamos el modelo 'Salary' para poder usarlo en nuestras Vistas CRUD
from .models import Salary

# Create your views here.
class SalaryList(ListView): 
    model = Salary # Llamamos a la clase 'Salary' que se encuentra en nuestro archivo 'models.py'