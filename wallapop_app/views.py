from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView


from .models import Anunci
from .models import Usuari
from .models import Comentari

from django.contrib.auth.models import User


from .forms import UpdateUserForm, UpdateProfileForm,AnunciForm


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.


def anunci_view(request):
   anunci = Anunci.objects.all()
   context = {
        'anunci_objects' : anunci,
    }
   return render(request, 'anuncis.html', context)

def get_anunci(request, iden):
    # try:
    #    obj = Post.objects.get(id=postid)
    # except Post.DoesNotExist:
    #    raise Http404
    obj = get_object_or_404(Anunci, id=iden)

    
    context = {
        'anunci' : obj,
    }
    return render(request, 'anunci-details.html', context)




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



@login_required
def edit_profile(request):
    return render(request, 'profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

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

def veureperfil(request,name):
    usuari = get_object_or_404(User, username=name)

    # Joan Jaume:Would like to acces our One to One Usuari model, but as usuari beeing an instance
    #we cannot do that. As well we tried to achive doing that by filtering our query and retrive
    #our Usuari model to display all of their things like bio, but that ain't the right way.

    anuncis = Anunci.objects.all()
    # anuncis1 = None
    # for anunci in anuncis:
    #     str = anunci.toString("d")
    #     if str == name:
    #         if anuncis1 == None:
    #             anuncis1 = anunci | anunci
    #         else:
    #             anuncis1 = anuncis1 |  anunci
            
    

    context = {
        'user' : usuari,
        'anuncis' : anuncis,
    }
    return render(request, 'profile_view.html', context)


