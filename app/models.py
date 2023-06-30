from django.db import models

class Producto(models.Model):

    codigo              = models.IntegerField()
    nombre              = models.CharField(max_length=20)
    precio              = models.IntegerField()
    descripcion         = models.TextField()
    imagen              = models.ImageField(upload_to="productos", null=True)  

    def __str__(self):
        return self.nombre


class contacto(models.Model):

    nombre              = models.CharField(max_length=50)
    correo            = models.EmailField()
    descripcion         = models.TextField()
    avisos                 = models.BooleanField()

    def __str__(self):
        return self.nombre


    
    
