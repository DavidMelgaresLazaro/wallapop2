from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView




#framework
from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import AnunciSerializer
from .serializers import UsuariSerializer


from .models import Anunci
from .models import Usuari
from .models import Comentari

from django.contrib.auth.models import User


from .forms import UpdateUserForm, UpdateProfileForm,AnunciForm,ComentariForm


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.



class AnunciViewSet(viewsets.ModelViewSet):
    queryset = Anunci.objects.all()
    serializer_class = AnunciSerializer
    permission_classes = [permissions.AllowAny]

class AnunciView_CLS(APIView):
    def get(self, request, the_anunci):
        try:
            anunci = Anunci.objects.get(pk=the_anunci)
        except:
            raise Http404
        serial = AnunciSerializer(anunci, context={'request':request})
        return Response(serial.data)

@api_view(['GET', 'DELETE'])
def AnunciView_FN(request, the_anunci):
    try:
        anunci = Anunci.objects.get(pk=the_anunci)
    except Anunci.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedanunci = AnunciSerializer(anunci, context={'request':request})
        return Response(data=serializedanunci.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        anunci.delete()
        return Response(status=status.HTTP_200_OK)

def index(request):
    return render(request, 'anuncis.html')


# def anunci_view(request):
#    anunci = Anunci.objects.all()
#    context = {
#         'anunci_objects' : anunci,
#     }
#    return render(request, 'anuncis.html', context)

# def get_anunci(request, iden):
#     # try:
#     #    obj = Post.objects.get(id=postid)
#     # except Post.DoesNotExist:
#     #    raise Http404
#     obj = get_object_or_404(Anunci, id=iden)

#     comments = Comentari.objects.all().filter(titol = obj)

#     comentari_form = ComentariForm(request.POST or None,titol = obj)

#     if request.user.is_authenticated:

#         if comentari_form.is_valid():
#             comentari_form.save()
#             messages.success(request, 'Anunci penjat')
#         #else:
#         # comentari_form = ComentariForm()


    
#     context = {
#         'anunci' : obj,
#         'comments' : comments,
#         'comentari' : comentari_form,
#     }
#     return render(request, 'anunci-details.html', context)

class UsuariViewSet(viewsets.ModelViewSet):
    queryset = Usuari.objects.all()
    serializer_class = UsuariSerializer
    permission_classes = [permissions.AllowAny]

class UsuariView_CLS(APIView):
    def get(self, request, the_anunci):
        try:
            anunci = Anunci.objects.get(pk=the_anunci)
        except:
            raise Http404
        serial = AnunciSerializer(anunci, context={'request':request})
        return Response(serial.data)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    usuari = get_object_or_404(Usuari, user=user)
    
    if request.method == 'GET':
        serializer = UsuariSerializer(usuari)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = UsuariSerializer(usuari, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    



def veureperfil(request,name):
    user = get_object_or_404(User, username=name)

    anuncis = Anunci.objects.all().filter(name = user)
    usuari = Usuari.objects.get(user = user)



    context = {
        'user' : user,
        'anuncis' : anuncis,
        'usuari' : usuari,
    }
    return render(request, 'profile_view.html', context)




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



@login_required
def edit_profile(request,username):
    usuari = get_object_or_404(User, username=username)
    UserName = Usuari.objects.get(user = usuari)
    form = UpdateProfileForm(request.POST,request.FILES , instance=UserName)

    if request.method == 'POST':
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            # return redirect('profile')


    context = {
        'user' : UserName,
        'name': form,
        
    }
    return render(request, 'profile.html',context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')

@login_required
def afegiranunci(request):
    anunci_form = AnunciForm(request.POST or None,request.FILES,user = request.user)
    if anunci_form.is_valid():
        anunci_form.save()
        messages.success(request, 'Anunci penjat')
        return redirect('/')
    else:
        anunci_form = AnunciForm(user = request.user)

    context = {
        'anunci' : anunci_form,
    }
    return render(request, 'add_anunci.html',context)

@login_required
def avatar(request):
    usuari_form = UpdateProfileForm(request.POST or None,request.FILES,user = request.user)
    if usuari_form.is_valid():
        usuari_form.save()
        messages.success(request, 'Foto cambiada penjat')
        return redirect('/')
    else:
        usuari_form = UpdateProfileForm(user = request.user)

    context = {
        'avatar_bio' : usuari_form,
    }
    return render(request, 'avatar.html',context)

def veureperfil(request,name):
    user = get_object_or_404(User, username=name)

    anuncis = Anunci.objects.all().filter(name = user)
    usuari = Usuari.objects.get(user = user)



    context = {
        'user' : user,
        'anuncis' : anuncis,
        'usuari' : usuari,
    }
    return render(request, 'profile_view.html', context)

    


