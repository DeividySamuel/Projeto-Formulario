from django.urls import path

from meusite.views import home

urlpatterns = [
    path('', home),  # Home
]