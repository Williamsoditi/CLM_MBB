from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'landing.html')

def contact(request):
    return render(request, 'contact.html')

def player_bios(request):
    return render(request, 'player_bios.html')

def schedule(request):
    return render(request, 'schedule.html')

