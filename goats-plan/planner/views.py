from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Task, ClientCompany, Project


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

# Doesn't work :(
class ClientCompanyAccessRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user

        # Ensure the user works on a project within the client company
        client_company_id = self.kwargs.get('id')  # Get UUID from URL
        try:
            client_company = ClientCompany.objects.get(id=client_company_id)
        except ClientCompany.DoesNotExist:
            return False

        user_projects = user.projects.all()
        return client_company.project_list.filter(id__in=user_projects.values_list('id', flat=True)).exists()


    def handle_no_permission(self):
        return redirect('planner:developer_page')


# Views
class Planner(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'Task'
    template_name = "planner/index.html"

class ProjectManagerHomeView(ProjectManagerRequiredMixin, ListView):
    model = ClientCompany
    context_object_name = 'Client Company'
    template_name = "planner/project_manager.html"

class DeveloperHomeView(DeveloperRequiredMixin, ListView):
    model = ClientCompany
    template_name = "planner/developer.html"
    #context_object_name = 'Client Company'

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


class ClientCompanyDetailView(DeveloperRequiredMixin, ClientCompanyAccessRequiredMixin, DetailView):
    model = ClientCompany
    template_name = 'planner/client_company_detail.html'
    #context_object_name = 'client_company'

    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        # Get the projects related to the client company
        client_company = self.get_object()
        context['projects'] = client_company.project_list.filter(user_list__in=[user])
        context['client_company'] = client_company

        return context

#TODO : add page to allow project manager to create and modify projects and companies and stuff

class ProjectDetailView(DetailView):
    model = Project
    #context_object_name = 'Task'
    template_name = 'planner/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project = self.get_object()

        user = self.request.user
        context['user_tasks'] = user.tasks.filter(project=project)

        return context