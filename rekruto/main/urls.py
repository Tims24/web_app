from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_message),
    path("hello/", views.index)
]
