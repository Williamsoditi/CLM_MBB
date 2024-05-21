from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    return render(request, 'landing.html')

def contact(request):
    return render(request, 'contact.html')

def player_bios(request):
    players = Player.objects.all()
    return render(request, 'player_bios.html', {
        'players': players
    })

def schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule.html', {
        'schedules':schedules
    })


