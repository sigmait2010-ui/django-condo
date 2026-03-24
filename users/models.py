from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Aquí después agregaremos cosas como 'departamento' o 'tipo_usuario'
    # Por ahora agregamos un teléfono de contacto como ejemplo
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username