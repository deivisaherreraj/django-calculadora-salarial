"""calculadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from salary.views import SalaryCreate, SalaryDelete, SalaryList, SalaryUpdate, SalaryView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # La ruta 'leer' en donde listamos todos los registros o salary de la Base de Datos
    path('salary/', SalaryList.as_view(template_name = "salary/index.html"), name='read'), 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un salary o registro 
    path('salary/view/<uuid:pk>', SalaryView.as_view(template_name = "salary/view.html"), name='view'), 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo salary o registro  
    path('salary/create', SalaryCreate.as_view(template_name = "salary/create.html"), name='create'), 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un salary o registro de la Base de Datos 
    path('salary/update/<uuid:pk>', SalaryUpdate.as_view(template_name = "salary/update.html"), name='update'),  
    # La ruta 'eliminar' que usaremos para eliminar un salary o registro de la Base de Datos 
    path('salary/delete/<uuid:pk>', SalaryDelete.as_view(), name='delete'),
]
