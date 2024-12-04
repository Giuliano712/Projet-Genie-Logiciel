from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'planner'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:userid>/mycompanies/', views.CompaniesView.as_view(), name='mycompanies'),
    #path('developer/', views.DeveloperHomeView.as_view(), name='developer_page'),
    #path('project_manager/', views.ProjectManagerHomeView.as_view(), name='project_manager_page'),
    path('<int:userid>/mycompanies/<uuid:ccid>/', views.ProjectsView.as_view(), name='myprojects'),
    path('<int:userid>/mycompanies/<uuid:ccid>/<uuid:projectid>/', views.TasksView.as_view(), name='mytasks'),
    path('<int:userid>/mycompanies/<uuid:ccid>/add-project/', views.ProjectCreateView.as_view(), name='add_project'),
]

# <uuid:id> uses the id of the clientcompany

#TODO : find a good path standard, maybe :
# /planner/<userid>/mycompanies/
#