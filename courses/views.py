from django.shortcuts import render

from .models import Home

def home(request):
    # Recupera o conteúdo da página home
    home = Home.objects.filter().first()
    return render(request, 'courses/home.html', { 'home': home})
