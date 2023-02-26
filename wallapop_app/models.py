from django.db import models


class Usuari(models.Model):
    name=models.CharField('Nombre', max_length=120)
    adress=models.CharField(max_length=300)
    zip_code=models.CharField('Codigo Postal', max_length=15)
    phone=models.CharField('Telefono de Conatcto', max_length=25)
    email=models.EmailField('Email de Contacto')

    def __str__(self):
        return self.name + self.adress +self.zip_code+ self.phone + self.email


class Anunci(models.Model):
    foto = models.ImageField('Imagen')
    titol = models.CharField('Asunto', max_length= 300)
    name = models.ForeignKey(Usuari,on_delete=models.CASCADE,blank=True,null=True)
    data = models.DateTimeField('Fecha Anuncio')
    description = models.TextField(blank=True)
    preu = models.IntegerField('Precio')
    

    def __str__(self):
        return self.foto + self.titol + self.description + self.preu + self.name + self.data
    



    
class Comentari(models.Model):
    name = models.ForeignKey(Usuari,on_delete=models.CASCADE,blank=True,null=True)
    titol = models.ForeignKey(Anunci,on_delete=models.CASCADE,blank=True,null=True)
    data_com = models.DateField('Fecha Comentario')
    id = models.IntegerField('ID', primary_key=True)



    def __str__(self):
        return self.name + self.titol + self.data_com + self.id