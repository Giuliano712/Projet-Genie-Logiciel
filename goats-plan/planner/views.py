from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tache
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView



class Planner(LoginRequiredMixin, ListView):
    model = Tache
    context_object_name = 'Tache'
    template_name = "planner/index.html"


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Tache
    context_object_name = 'task'  # Utilisez un nom pour accéder aux données dans le template
    template_name = "planner/task_detail.html"  # Chemin vers votre template HTML


