from django.urls import path
from . import views



app_name = 'planner'

urlpatterns = [
    path('', views.Planner.as_view(), name='planner_page'),
]
