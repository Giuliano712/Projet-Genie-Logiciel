from django import forms
from .models import ClientCompany, Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'user_list']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = ClientCompany
        fields = ['name', 'project_list'] # Allow selection of projects for the company

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'status', 'importance', 'deadline', 'assigned_users']