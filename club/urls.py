from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('newresource/', views.newResource, name='newresource'),
    path('getresource/', views.getResource, name='getresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]