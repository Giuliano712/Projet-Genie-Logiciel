from django.urls import path
from . import views


urlpatterns = [
    path("", views.Planning.as_view(), name="index"),
]