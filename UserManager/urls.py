from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registrationPage, name='registration'),
    path('create_profile/', views.profilePage, name='create-profile'),
    path('show_profile/', views.showProfile, name='show-profile'),
]
