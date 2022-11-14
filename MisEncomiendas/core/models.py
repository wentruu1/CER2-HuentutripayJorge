from django.db import models

# Create your models here.

ESTADO_CORRESPONDENCIA = [
    ("PENDIENTE", "Pendiente"),
    ("RECIBIDO", "Recibido"),
]

class Residencia(models.Model):
    casa = models.IntegerField()
    propietario = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.casa)

class Correspondencia(models.Model):
    fecha = models.DateTimeField()
    casa = models.ForeignKey(Residencia, on_delete=models.CASCADE)
    estado = models.CharField(max_length = 20, choices = ESTADO_CORRESPONDENCIA, default = "PENDIENTE")
    destinatario = models.CharField(max_length = 100, null=True, default = "No especificado")
    def __str__(self):
        return str(self.fecha.day) + "-" + str(self.fecha.month) + "-" + str(self.fecha.year) + " Para: "+ str(self.casa) 