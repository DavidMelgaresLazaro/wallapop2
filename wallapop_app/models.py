from django.db import models

# Create your models here.

class Anunci(models.Model):
    foto = models.ImageField()
    titol = models.TextField()
    description = models.TextField()
    preu = models.TextField()
    ubi = models.TextField()

    def __str__(self):
        return self.foto + self.titol + self.description + self.preu + self.ubi