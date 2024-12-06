from django.contrib import admin
from .models import Task, ClientCompany, Project

admin.site.register(Task)
admin.site.register(ClientCompany)
admin.site.register(Project)
