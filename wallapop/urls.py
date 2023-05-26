"""wallapop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from wallapop_app.views import SignUpView,edit_profile,ChangePasswordView,afegiranunci,profile,afegiranunci,index,index_details

from rest_framework import routers
from wallapop_app import views

from rest_framework.authtoken import views as viewstoken 

from django.urls import path

from wallapop_app import views as views2




router = routers.DefaultRouter()
router.register(r'anuncis', views.AnunciViewSet)
router.register(r'comentaris', views.ComentariViewSet)
# router.register(r'usuaris_view')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('' , index ,name="anuncis"),#/home
    path('api/',include(router.urls)),
    path('',index,name="anuncis"),
    path('api/anunci/<int:the_anunci>/', include(router.urls)),
    path('api/comentaris/<int:the_comentari>/', include(router.urls)),
    path('api/agefir-comentari/', include(router.urls)),
    path('anuncis/<int:pk>/',index_details,name="anunci-details"),
    path('api/anuncis/<int:pk>/', views2.AnunciView_FN),
    path('api/profile/<str:username>/', views2.AnunciView_FN),
    path('accounts/',include("django.contrib.auth.urls")),
    path('signup', SignUpView.as_view(), name="signup"),
    path('profile/<str:username>/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', edit_profile, name='profile'),
    # path('anunci-details/<int:iden>/', get_anunci, name='anunci-details'),
    path('users/<str:name>/', profile, name='usuaris'),
    path('password-change/', ChangePasswordView.as_view(), name='password-change'),
    path('add_anunci/', afegiranunci ,name='add_anunci'),
    path('api-token-auth/', viewstoken.obtain_auth_token),

    path('router/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
