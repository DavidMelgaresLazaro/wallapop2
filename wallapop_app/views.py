from django.shortcuts import render

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


