from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tache


class Planning(ListView):
    model = Tache
    context_object_name = 'Tache'
    template_name = "Planifieur/index.html"