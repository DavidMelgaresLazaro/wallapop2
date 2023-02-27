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
    titol = forms.CharField(widget=forms.Textarea,max_length= 300)
    description = forms.CharField(widget=forms.Textarea,max_length=500)
    preu = forms.IntegerField(widget=forms.Textarea)
    def __init__(self, user, *args, **kwargs):
        super(AnunciForm, self).__init__(*args, **kwargs)
        self.user = user
        self.name = forms.CharField(initial = user)
        
