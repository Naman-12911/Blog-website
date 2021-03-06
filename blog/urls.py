from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [ 
   path('postComment',views.postComment, name = "postComment"),  # Api to post comments
   path('', views.blogHome, name='blogHome'), 
   path('<str:slug>', views.blogPost, name='blogPost'), 
]