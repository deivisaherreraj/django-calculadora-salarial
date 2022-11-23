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

class SalaryView(DetailView): 
    model = Salary # Llamamos a la clase 'Salary' que se encuentra en nuestro archivo 'models.py'
    
class SalaryCreate(SuccessMessageMixin, CreateView): 
    model = Salary # Llamamos a la clase 'Salary' que se encuentra en nuestro archivo 'models.py'
    form = Salary # Definimos nuestro formulario con el nombre de la clase o modelo 'Salary'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Salary' de nuestra Base de Datos 
    success_message = 'Salario creada correctamente !' # Mostramos este mensaje luego de crear una salario
 
    # Redireccionamos a la página principal luego de crear un registro o salario
    def get_success_url(self):        
        return reverse('read') # Redireccionamos a la vista principal 'leer'

class SalaryUpdate(SuccessMessageMixin, UpdateView): 
    model = Salary # Llamamos a la clase 'Salary' que se encuentra en nuestro archivo 'models.py' 
    form = Salary # Definimos nuestro formulario con el nombre de la clase o modelo 'Salary' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Person' de nuestra Base de Datos 
    success_message = 'Salary actualizado correctamente !' # Mostramos este mensaje luego de editar una salario
 
    # Redireccionamos a la página principal luego de actualizar un registro o salario
    def get_success_url(self):               
        return reverse('read') # Redireccionamos a la vista principal 'leer'

class SalaryDelete(SuccessMessageMixin, DeleteView): 
    model = Salary 
    form = Salary
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o salario
    def get_success_url(self): 
        success_message = 'Salary eliminado correctamente !' # Mostramos este mensaje luego de editar una salario 
        messages.success(self.request, (success_message))       
        return reverse('read') # Redireccionamos a la vista principal 'leer'