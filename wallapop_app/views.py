from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from .models import Anunci
from .models import Usuari
from .models import Comentari


# Create your views here.


def anunci_view(request):
   anunci = Anunci.objects.all()
   context = {
        'anunci_objects' : anunci,
    }
   return render(request, 'anuncis.html', context)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"