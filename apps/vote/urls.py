from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("pcNuYtBIFmyXMOsOYUUn", views.submit, name="vote")
]
