from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Planifieur'

urlpatterns = [
    path('', views.Planning.as_view(), name='planning_page'),
]