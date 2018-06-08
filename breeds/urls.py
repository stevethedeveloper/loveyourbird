"""Defines URL patterns for breeds."""

from django.urls import path

from . import views

app_name='breeds'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:breed_id>/breed', views.detail, name='detail'),
]
