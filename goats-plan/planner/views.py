from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView
from .models import Task, ClientCompany, Project
from .forms import ProjectForm, CompanyForm, TaskForm


# Mixins
class ProjectManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'project_manager'

    def handle_no_permission(self):
        return redirect('users:login')  # Redirect to login page or a different page

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
        return redirect(reverse('planner:mycompanies', kwargs={'userid': self.request.user.id}))


# Views
class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        #return redirect(reverse('planner:mycompanies', kwargs={'userid': self.request.user.id}))
        return redirect('planner:mycompanies', userid=request.user.id)

class MyCompaniesView(LoginRequiredMixin, View):
    model = ClientCompany

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        # redirect user based on role
        if request.user.role == 'developer':
            return render(request, 'planner/developer/companies.html', context)
        elif request.user.role == 'project_manager':
            return render(request, 'planner/project_manager/companies.html', context)

        return redirect('users:login')

    def get_context_data(self):
        context = {}

        # Get the logged-in user
        user = self.request.user
        # Get the projects the user is involved in
        user_projects = user.get_projects()
        # Get the ClientCompanies that are related to these projects
        client_companies = ClientCompany.objects.filter(project_list__in=user_projects).distinct()
        context['client_companies'] = client_companies

        return context


class ClientCompanyDetailView(LoginRequiredMixin, DetailView):
    model = ClientCompany
    #template_name = 'planner/developer/projects.html'

    pk_url_kwarg = 'ccid'

    def get_template_names(self):
        if self.request.user.role == 'developer':
            return ['planner/developer/projects.html']
        elif self.request.user.role == 'project_manager':
            return ['planner/project_manager/projects.html']

        return ['planner/not_found.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        # Get the projects related to the client company
        client_company = self.get_object()
        context['projects'] = client_company.project_list.filter(user_list__in=[user])
        context['client_company'] = client_company

        return context

#TODO : add page to allow project manager to create and modify projects and tasks and stuff

# this class displays the tasks
class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    #template_name = 'planner/developer/tasks.html'

    pk_url_kwarg = 'projectid'

    def get_template_names(self):
        user = self.request.user
        if user.role == 'developer':
            return ['planner/developer/tasks.html']
        elif user.role == 'project_manager':
            return ['planner/project_manager/tasks.html']

        return ['planner/not_found.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project = self.get_object()

        user = self.request.user
        context['user_tasks'] = user.tasks.filter(project=project)

        parent_company = project.companies.first()
        context['parent_company'] = parent_company

        return context

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'planner/project_manager/create_project.html'

    #pk_url_kwarg = 'ccid'

    def form_valid(self, form):
        project = form.save(commit=False)

        # automatically add project manager on project creation
        if self.request.user not in form.instance.user_list.all():
            project.user_list.add(self.request.user)
        # Retrieve the ClientCompany ID from the URL kwargs
        client_company_id = self.kwargs.get('ccid')
        try:
            client_company = ClientCompany.objects.get(id=client_company_id)
            project.save()  # Save the project to generate the primary key
            client_company.project_list.add(project)  # Link the project to the company
        except ClientCompany.DoesNotExist:
            return redirect('planner:home')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ccid = self.kwargs.get('ccid')
        try:
            parent_company = ClientCompany.objects.get(id=ccid)
            context['parent_company'] = parent_company
        except ClientCompany.DoesNotExist:
            context['parent_company'] = None  # Handle case where company doesn't exist
        return context

    def get_success_url(self, **kwargs):
        return reverse('planner:myprojects', kwargs={'userid': self.request.user.id, 'ccid': self.kwargs.get('ccid')})


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'planner/project_manager/create_project.html'

    pk_url_kwarg = 'projectid'

    def get_object(self, queryset=None):
        project = super().get_object(queryset)
        return project

    def form_valid(self, form):
        # Call the superclass method to save the updated project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ccid = self.kwargs.get('ccid')
        try:
            parent_company = ClientCompany.objects.get(id=ccid)
            context['parent_company'] = parent_company
        except ClientCompany.DoesNotExist:
            context['parent_company'] = None  # Handle case where company doesn't exist

        return context

    def get_success_url(self):
        # Redirect to the project details page (or wherever appropriate)
        return reverse('planner:myprojects', kwargs={'userid': self.request.user.id, 'ccid': self.kwargs.get('ccid')})


class TaskCreateView(ProjectManagerRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'planner/project_manager/create_task.html'

    def form_valid(self, form):
        task = form.save(commit=False)

        projectid = self.kwargs.get('projectid')
        try:
            parent_project = Project.objects.get(id=projectid)
            # automatically set parent project as project
            task.project = parent_project
            task.save()  # Save the project to generate the primary key
        except ClientCompany.DoesNotExist:
            return redirect('planner:home')

        return super().form_valid(form)

    def get_success_url(self):
        projectid = self.kwargs.get('projectid')
        return reverse('planner:mytasks', kwargs={'userid': self.request.user.id, 'ccid': self.kwargs.get('ccid'), 'projectid': projectid})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ccid = self.kwargs.get('ccid')
        projectid = self.kwargs.get('projectid')
        try:
            parent_project = Project.objects.get(id=projectid)
            context['parent_project'] = parent_project
        except Project.DoesNotExist:
            context['parent_project'] = None
        try:
            parent_company = ClientCompany.objects.get(id=ccid)
            context['parent_company'] = parent_company
        except ClientCompany.DoesNotExist:
            context['parent_company'] = None  # Handle case where company doesn't exist

        print(f"parent_company: {context['parent_company']}, parent_project: {context['parent_project']}")

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Pass the parent project to the form as initial data
        projectid = self.kwargs.get('projectid')
        try:
            parent_project = Project.objects.get(id=projectid)
            kwargs['initial'] = {'project': parent_project}
        except Project.DoesNotExist:
            kwargs['initial'] = {'project': None}
        return kwargs


class TaskUpdateView(ProjectManagerRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'planner/task_form.html'

    def get_success_url(self):
        return redirect('planner:task_detail', pk=self.object.pk)  # Redirect to the updated task detail