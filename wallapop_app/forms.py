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


class AnunciForm(forms.Form):
    foto = forms.ImageField()
    titol = forms.CharField(max_length= 300)
    data = forms.DateTimeField(initial=timezone.now)
    description = forms.CharField(max_length=500)
    preu = forms.IntegerField()
    def __init__(self, user, *args, **kwargs):
        super(AnunciForm, self).__init__(*args, **kwargs)
        self.user = user
        self.name = forms.CharField(initial= user,max_length=100)


class PostAnunciForm(forms.ModelForm):
    class Meta:
        model = Anunci
        fields = [
            'foto',
            'titol',
            'name',
            'data',
            'description',
            'preu',
        ]
    def clean_image(self):
        img = self.cleaned_data.get('image')
        if not img:
            return img
        maxdim = 1024
        if any(dim > maxdim for dim in img.image.size):
            # Resize too large image up to the max_size
            from PIL import Image
            i = Image.open(img.file)
            fmt = i.format.lower()
            i.thumbnail((maxdim, maxdim))
            # We must reset io.BytesIO object, otherwise resized image bytes
            # will get appended to the original image  
            img.file = type(img.file)()
            i.save(img.file, fmt)
        return img