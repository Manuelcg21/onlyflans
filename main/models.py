import uuid
from django.db import models

# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(max_length=64)
    email = models.CharField(max_length=15)
    mensaje = models.CharField(max_length=64,null=False)

class Flan(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField()
    precio = models.IntegerField(default=1000)
    imagen_url = models.URLField()
    is_private = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.nombre