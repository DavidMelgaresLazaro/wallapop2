from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView


from .models import Anunci
from .models import Usuari
from .models import Comentari

from .forms import UpdateUserForm, UpdateProfileForm,AnunciForm,PostAnunciForm


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

def get_anunci(request, name):
    # try:
    #    obj = Post.objects.get(id=postid)
    # except Post.DoesNotExist:
    #    raise Http404
    obj = get_object_or_404(Anunci, id=name)

    
    context = {
        'anunci' : obj,
=======

    context = {
        'post' : obj,
>>>>>>> 2049eb3 (Merge branch 'master' of https://github.com/emuajj/wallapop)
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