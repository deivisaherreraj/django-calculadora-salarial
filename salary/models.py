import uuid
from django.db import models

GERENTE = 'l'
SECRETARIA = '2'
CAJERO = '3'

POSITION = (
    (GERENTE, 'Gerente'),
    (SECRETARIA, 'Secretaria'),
    (CAJERO, 'Cajero')
)

# Creación de campos de la tabla 'salary' 
class Salary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=5, choices=POSITION, default=GERENTE)
    hours = models.IntegerField(blank=True, null=True)
    years = models.IntegerField(blank=True, null=True)
 
    class Meta:
        db_table = 'salary'