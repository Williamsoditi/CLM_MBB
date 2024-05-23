from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('player_bios/', views.player_bios, name='player_bios'),
    path('schedule/', views.schedule, name='schedule'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]