"""projetWEB URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from MarseilleInsiderApp.views import vw_home,vw_activities,vw_activities_cat_filter,vw_activity,inscription,vw_packs,vw_pack,compte_client,ClientUpdateView,CustomPasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',vw_home),
    path('activities/',vw_activities),
    path('activities/<str:categorie>/',vw_activities_cat_filter),
    path('activity/<int:id_loisir>/',vw_activity, name='activity_detail'),
    path('inscription/', inscription, name='inscription'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('packs/',vw_packs),
    path('pack/<int:id_pack>/',vw_pack),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('compte/',compte_client, name="compte"),
    path('compte/client_update/', ClientUpdateView.as_view(), name='client_update'),
]
