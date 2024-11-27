from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tache


class Planning(LoginRequiredMixin, ListView):
    model = Tache
    context_object_name = 'Tache'
    template_name = "Planifieur/index.html"