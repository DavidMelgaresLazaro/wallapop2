from django import forms
from django.utils import timezone

from django.contrib.auth.models import User
from .models import Profile,Anunci



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class AnunciForm(forms.ModelForm):
    foto = forms.ImageField(widget=forms.FileInput)
    titol = forms.CharField(widget=forms.Textarea,help_text="Titol")
    description = forms.Textarea()
    preu = forms.IntegerField(widget=forms.Textarea,help_text="Preu")
    # def __init__(self, user, *args, **kwargs):
    #     super(AnunciForm, self).__init__(*args, **kwargs)
    #     self.user = user
    #     self.name = forms.CharField(self.user)
    class Meta:
        model = Anunci
        exclude = ["name","data"]
        fields = [
            'foto',
            'titol',
            'description',
            'preu',
        ]
    # def clean_image(self):
    #     foto = self.cleaned_data.get('foto')
    #     if not foto:
    #         return foto
    #     maxdim = 1024
    #     if any(dim > maxdim for dim in foto.image.size):
    #         # Resize too large image up to the max_size
    #         from PIL import Image
    #         i = Image.open(foto.file)
    #         fmt = i.format.lower()
    #         i.thumbnail((maxdim, maxdim))
    #         # We must reset io.BytesIO object, otherwise resized image bytes
    #         # will get appended to the original image  
    #         foto.file = type(foto.file)()
    #         i.save(foto.file, fmt)
    #     return foto
    # def errors(self):
    #     print(self.errors)
    #     print(self.non_field_errors)
    
        
