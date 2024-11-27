from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'planner'

urlpatterns = [
    path('', views.Planner.as_view(), name='planner_page'),
]