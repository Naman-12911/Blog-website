from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [ 
   path('', views.home, name='home'),
   path('tiny', views.tiny, name='tiny'),
   path('contact', views.contact, name='contact'),
   path('search', views.search, name='search'),
   path('sinup', views.sinup, name='sinup'),
   path('login', views.loginhandle, name='login'),
   path('logout', views.handleLogout, name='handleLogout'),
]