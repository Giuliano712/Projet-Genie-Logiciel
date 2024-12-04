from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Tache, ClientCompany


# Mixins
class ProjectManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'project_manager'

    def handle_no_permission(self):
        return redirect('users:login')

class DeveloperRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'developer'

    def handle_no_permission(self):
        return redirect('users:login')


# Views
class Planner(LoginRequiredMixin, ListView):
    model = Tache
    context_object_name = 'Tache'
    template_name = "planner/index.html"

class ProjectManagerHomeView(ProjectManagerRequiredMixin, ListView):
    model = ClientCompany
    context_object_name = 'Client Company'
    template_name = "planner/project_manager.html"

class DeveloperHomeView(DeveloperRequiredMixin, ListView):
    model = ClientCompany
    context_object_name = 'Client Company'
    template_name = "planner/developer.html"

    def get_context_data(self, **kwargs):
        # Get the logged-in user
        user = self.request.user

        # Get the projects the user is involved in
        user_projects = user.get_projects()

        # Get the ClientCompanies that are related to these projects
        client_companies = ClientCompany.objects.filter(project_list__in=user_projects).distinct()

        context = super().get_context_data(**kwargs)
        context['client_companies'] = client_companies
        return context


class ClientCompanyDetailView(DetailView):
    model = ClientCompany
    template_name = 'planner/client_company_detail.html'
    context_object_name = 'client_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the projects related to the client company
        client_company = self.get_object()
        context['projects'] = client_company.project_list.all()

        return context

#TODO : add page to allow project manager to create and modify projects and companies and stuff