from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Modelo de Administrador
class Administrador(models.Model):
    """ Administrador del sistema """
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    telefono = models.CharField(max_length=15, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('administrador-list')

# Modelo de Mascota
class Mascota(models.Model):
    """ Mascota disponible para adopción """
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]
    
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    edad = models.PositiveIntegerField()  
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='mascotas/')
    estado_adopcion = models.CharField(max_length=20, default='Disponible')
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('mascota-list')

# Modelo de Solicitud de Adopción
class SolicitudAdopcion(models.Model):
    """ Solicitud de adopción de una mascota """
    ESTADO_SOLICITUD_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
    ]
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='solicitudes')
    nombre_solicitante = models.CharField(max_length=100)
    email_solicitante = models.EmailField()
    telefono_solicitante = models.CharField(max_length=15)
    direccion_solicitante = models.CharField(max_length=200)
    observaciones = models.TextField(blank=True)
    estado_solicitud = models.CharField(max_length=10, choices=ESTADO_SOLICITUD_CHOICES, default='Pendiente')

    def __str__(self):
        return f'Solicitud de {self.nombre_solicitante} para {self.mascota.nombre}'
    
    def get_absolute_url(self):
        return reverse('solicitud-list')

@receiver(post_delete, sender=Mascota)
def mascota_delete(sender, instance, **kwargs):
    """ Borra los archivos de imagen al eliminar la mascota """
    instance.imagen.delete(False)


