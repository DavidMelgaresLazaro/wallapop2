from django.shortcuts import render

from .models import Anunci

# Create your views here.


def anunci_view(request):
    anunci = Anunci.objects.all()
    context = {
        'anunci_objects' : anunci,
    }
    return render(request, 'anuncis.html', context)