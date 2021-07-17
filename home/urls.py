from django_email_verification import urls as email_urls
from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views
from django_email_verification import urls as email_urls

urlpatterns = [ 
   path('', views.home, name='home'),
   path('tiny', views.tiny, name='tiny'),
   path('contact', views.contact, name='contact'),
   path('search', views.search, name='search'),
   path('sinup', views.sinuphandle, name='sinup'),
   path('login', views.loginhandle, name='login'),
   path('email/', include(email_urls)),
   path('logout',views.logouthandle,name = 'logout'),
   path('reset_password/', auth_views.PasswordResetView.as_view(template_name="home/password_reset.html"),
        name="reset_password"),
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_sent.html"),
        name="password_reset_done"),

   path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_form.html"),
        name="password_reset_confirm"),

   path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
       template_name="home/password_reset_done.html"), name="password_reset_complete"),
]