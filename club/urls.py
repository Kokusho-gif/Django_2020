from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('newresource/', views.newResource, name='newresource'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('getresource/', views.getResource, name='getresource'),
    path('getmeeting/', views.getMeeting, name='getmeeting'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]