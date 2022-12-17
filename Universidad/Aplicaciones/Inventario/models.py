from django.db import models

# Create your models here.


class EquiposComputo(models.Model):
    codigo_activo_fijo = models.CharField(primary_key=True, max_length=30)
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=20)

    def __str__(self):
        texto = "{0} {1} {2} {3} {4}"
        return texto.format(self.codigo_activo_fijo, self.tipo, self.marca, self.modelo, self.color)
