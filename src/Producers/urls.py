from django.urls import path
from . import views

app_name="producers"

urlpatterns = [
    path('', views.index),
]
