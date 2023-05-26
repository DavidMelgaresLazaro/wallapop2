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
from rest_framework.authtoken.models import Token

from .serializers import AnunciSerializer,UsuariSerializer,ComentariSerializer,UserSerializer


from .models import Anunci
from .models import Usuari
from .models import Comentari

from django.contrib.auth.models import User


from .forms import UpdateUserForm, UpdateProfileForm,AnunciForm,ComentariForm


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required






# Create your views here.

class ComentariViewSet(viewsets.ModelViewSet):
    queryset = Comentari.objects.all()
    serializer_class = ComentariSerializer
    permission_classes = [permissions.AllowAny]
    basename = 'comentari'
    def get_queryset(self):
        print("paso")
        queryset = Comentari.objects.all()
        anunci_id = self.kwargs.get('anunci_id') 
        if anunci_id is not None:
            queryset = queryset.filter(titol=anunci_id)
        return queryset

class AnunciViewSet(viewsets.ModelViewSet):
    queryset = Anunci.objects.all()
    serializer_class = AnunciSerializer
    permission_classes = [permissions.AllowAny]

class AnunciView_CLS(APIView):
    def get(self, request, the_anunci):
        try:
            anunci_serializer = Anunci.objects.get(the_anunci, context={'request': request})
            comments = Comentari.objects.filter(titol=the_anunci)
            comments_serializer = ComentariSerializer(comments, many=True)
        except:
            raise Http404
        data = {
            'anunci': anunci_serializer.data,
            'comments': comments_serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)

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
def index_details(request,pk):
    ctx = {'ad_id':pk}
    return render(request, 'anunci-details.html',context=ctx)



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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    



# class UsuariView_CLS(APIView):
#     def get(self, request, the_anunci):
#         try:
#             anunci = Anunci.objects.get(pk1=the_anunci)
#         except:
#             raise Http404
#         serial = AnunciSerializer(anunci, context={'request':request})
#         return Response(serial.data)

# @api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def edit_profile(request, username):
#     user = get_object_or_404(User, username=username)
#     usuari = get_object_or_404(Usuari, user=user)
    
#     if request.method == 'GET':
#         serializer = UsuariSerializer(usuari)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = UsuariSerializer(usuari, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
# def profile(request):
#     return render(request, 'profile.html')



# def veureperfil(request,name):
#     user = get_object_or_404(User, username=name)

#     anuncis = Anunci.objects.all().filter(name = user)
#     usuari = Usuari.objects.get(user = user)



#     context = {
#         'user' : user,
#         'anuncis' : anuncis,
#         'usuari' : usuari,
#     }
#     return render(request, 'profile_view.html', context)




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"




@api_view(['GET', 'PUT', 'POST'])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return Response({'message': 'Your profile is updated successfully'})
        else:
            return Response({'errors': user_form.errors + profile_form.errors}, status=400)
    
    elif request.method == 'PUT':
        user_form = UpdateUserForm(request.data, instance=request.user)
        profile_form = UpdateProfileForm(request.data, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return Response({'message': 'Your profile is updated successfully'})
        else:
            return Response({'errors': user_form.errors + profile_form.errors}, status=400)
    
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    user_data = {'username': request.user.username, 'email': request.user.email}  # Customize the user data as needed
    profile_data = {'profile_picture': request.user.profile.profile_picture.url}  # Customize the profile data as needed

    return Response({'user_form': user_data, 'profile_form': profile_data})


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


    


