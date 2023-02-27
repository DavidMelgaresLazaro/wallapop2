from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.urls import reverse

from .models import User







class Usuari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField('Nombre', max_length=120)
    adress=models.CharField(max_length=300)
    zip_code=models.CharField('Codigo Postal', max_length=15)
    phone=models.CharField('Telefono de Conatcto', max_length=25)
    email=models.EmailField('Email de Contacto')

    avatar=models.ImageField(upload_to='profile_images', blank=True, null=True)

    bio = models.TextField(max_length=300)


    def __str__(self):
       return self.name + ' , '+self.email

    def get_absolute_url(self):
        return reverse('profile_view', kwargs={'user':self.id})



class Anunci(models.Model):
    foto = models.ImageField('Imagen')
    titol = models.CharField('Asunto', max_length= 300)
    name = models.ForeignKey(Usuari,on_delete=models.CASCADE,blank=True,null=True)
    data = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    preu = models.IntegerField('Precio')
    

    def __str__(self):
        return self.titol + ' , ' + str(self.data) + ' , ' + str(self.name)
    
    def get_absolute_url(self):
        return reverse('anunci-details', kwargs={'name':self.id})
    
class AnunciModelForm(ModelForm):
    class Meta:
        model = Anunci
        exclude = ['date','name']
        fields = [
            'foto',
            'titol',
            'description',
            'preu',
        ]
    def clean_image(self):
        foto = self.cleaned_data.get('image')
        if not foto:
            return foto
        maxdim = 1024
        if any(dim > maxdim for dim in foto.image.size):
            # Resize too large image up to the max_size
            from PIL import Image
            i = Image.open(foto.file)
            fmt = i.format.lower()
            i.thumbnail((maxdim, maxdim))
            # We must reset io.BytesIO object, otherwise resized image bytes
            # will get appended to the original image  
            foto.file = type(foto.file)()
            i.save(foto.file, fmt)
        return foto



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    






    
class Comentari(models.Model):
    name = models.ForeignKey(Usuari,on_delete=models.CASCADE,blank=True,null=True)
    titol = models.ForeignKey(Anunci,on_delete=models.CASCADE,blank=True,null=True)
    data_com = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    id = models.IntegerField('ID', primary_key=True)



    def __str__(self):
        return str(self.titol) + ' , '+ str(self.id)