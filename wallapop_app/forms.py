from django import forms
from django.utils import timezone

from django.contrib.auth.models import User
from .models import Profile,Anunci,Comentari,Usuari



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
    name=forms.CharField(widget=forms.Textarea,help_text="Name")
    adress=forms.CharField(widget=forms.Textarea,help_text="Adress")
    zip_code=forms.CharField(widget=forms.Textarea,help_text="zip")
    email=forms.CharField(widget=forms.Textarea,help_text="email")
    phone=forms.CharField(widget=forms.Textarea,help_text="phone")
    avatar=forms.ImageField(widget=forms.FileInput,help_text="avatar")
    bio = forms.CharField(widget=forms.Textarea,help_text="bio")
    class Meta:
        model = Usuari
        exclude = ["user"]
        fields = ['avatar', 'bio']


class AnunciForm(forms.ModelForm):
    foto = forms.ImageField(widget=forms.FileInput)
    titol = forms.CharField(widget=forms.Textarea,help_text="Titol")
    description = forms.Textarea()
    preu = forms.IntegerField(widget=forms.Textarea,help_text="Preu")
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('user')
        super(AnunciForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Anunci
        exclude = ["name","data"]
        fields = [
            'foto',
            'titol',
            'description',
            'preu',
        ]
    def save(self, commit=True):
        inst = super(AnunciForm, self).save(commit=False)
        inst.name = self.name
        if commit:
            inst.save()
            self.save_m2m()
        return inst
    
class ComentariForm(forms.ModelForm):
    description = forms.Textarea()
    def __init__(self, *args, **kwargs):
        self.titol = kwargs.pop('titol')
        super(ComentariForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Comentari
        exclude = ["titol","name","data_com"]
        fields = [
            'description',
        ]
    def save(self, commit=True):
        inst = super(ComentariForm, self).save(commit=False)
        inst.titol = self.titol
        if commit:
            inst.save()
            self.save_m2m()
        return inst
    
        
