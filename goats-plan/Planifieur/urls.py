from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register_view


urlpatterns = [
    path('', register_view, name='register'),
    path('', views.Planning.as_view(), name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]