from django import forms
from .models import ClientCompany, Project, Task
from users.models import CustomUser


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
        fields = ['title', 'description', 'status', 'importance', 'deadline', 'assigned_users']

    # only add users that work on the task's project
    def __init__(self, *args, **kwargs):
        # Get the project from kwargs passed to the form instance
        project = kwargs.get('initial', {}).get('project', None)

        super().__init__(*args, **kwargs)

        # Filter the user choices to only include users related to the project
        if project:
            self.fields['assigned_users'].queryset = project.user_list.all()
        else:
            self.fields['assigned_users'].queryset = CustomUser.objects.none()  # No users if no project is provided

class TaskUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']