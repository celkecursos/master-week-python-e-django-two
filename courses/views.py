from django.shortcuts import render, redirect
from .forms import ContactForm

from django.contrib import messages
from .models import Home

def home(request):
    # Recupera o conteúdo da página home
    home = Home.objects.filter().first()
    return render(request, 'courses/home.html', { 'home': home})

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect('contact')
        else:
            messages.error(request, "Erro ao enviar a mensagem!")
    else:
        form = ContactForm()

    return render(request, 'courses/contact.html', { 'form': form })
