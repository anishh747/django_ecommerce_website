"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from home import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('index',views.index1,name='home2'),
    path('register',views.register,name='register'),
    path("login", views.login,name='login'),
    path("logout", views.logoutUser,name='loout'),
    path("contacts",views.contacts,name='contacts'),
    path("contacts1",views.contacts1,name='contacts1'),
    path('about',views.about,name='about'),
    path('about1',views.about1,name='about1'),
    path('payment',views.payment,name='pay'),
    path('item1',views.item1,name='item1'),
    path('item2',views.item2,name='item2'),
    path('item3',views.item3,name='item3'),
    path('item4',views.item4,name='item4'),
    path('item5',views.item5,name='item5'),
    path('item6',views.item6,name='item6'),
    path('item7',views.item7,name='item7'),
    path('item8',views.item8,name='item8'),
    path('item9',views.item9,name='item9'),

] 
