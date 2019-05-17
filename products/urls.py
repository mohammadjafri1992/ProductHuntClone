from django.urls import path

from .views import create, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create, name='create'),


]
