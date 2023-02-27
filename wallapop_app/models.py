from django.db import models
from django.utils import timezone



class Usuari(models.Model):
    name=models.CharField('Nombre', max_length=120)
    adress=models.CharField(max_length=300)
    zip_code=models.CharField('Codigo Postal', max_length=15)
    phone=models.CharField('Telefono de Conatcto', max_length=25)
    email=models.EmailField('Email de Contacto')

    def __str__(self):
        return self.name + ' , '+self.email


class Anunci(models.Model):
    foto = models.ImageField('Imagen')
    titol = models.CharField('Asunto', max_length= 300)
    name = models.ForeignKey(Usuari,on_delete=models.CASCADE,blank=True,null=True)
    data = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    preu = models.IntegerField('Precio')
    

    def __str__(self):
        return self.titol + ' , ' + str(self.data) + ' , ' + str(self.name)



    
class Comentari(models.Model):
    name = models.ForeignKey(Usuari,on_delete=models.CASCADE,blank=True,null=True)
    titol = models.ForeignKey(Anunci,on_delete=models.CASCADE,blank=True,null=True)
    data_com = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    id = models.IntegerField('ID', primary_key=True)



    def __str__(self):
        return str(self.titol) + ' , '+ str(self.id)