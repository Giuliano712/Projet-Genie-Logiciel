from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tache
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


class Planning(ListView):
    model = Tache
    context_object_name = 'Tache'
    template_name = "Planifieur/index.html"

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après inscription
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})