"""mtkkaGame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from game import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include

urlpatterns = [
    path("",views.index, name= 'index'),
    path("weeklyChart", views.weeklyChart, name='weeklyChart'),
    path("allMarket", views.allMarket, name='allMarket'),
    path("gussingFrom", views.gussingFrom, name= 'gussingFrom'),
    path("bharathjodi", views.bharathjodi, name= 'bharathjodi'),
    path("milanDay", views.milanDay, name= 'milanDay'),
    path("sriDevi", views.sriDevi, name= 'sriDevi'),
    path("timeBazar", views.timeBazar, name= 'timeBazar'),
    path("panelBharath", views.panelBharath, name= 'panelBharath'),
    path("panelmilan", views.panelmilan, name= 'panelmilan'),
    path("panelseridevi", views.panelseridevi, name= 'panelseridevi'),
    path("paneltime", views.paneltime, name= 'paneltime'),
    path("playGame", views.playGame, name= 'playGame'),
    path("Signup", views.handleSignUp, name= 'handleSignUp'),
    path("login", views.handlelogin, name= 'handlelogin'),
    path("logout", views.handlelogout, name= 'handlelogout')
   
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
