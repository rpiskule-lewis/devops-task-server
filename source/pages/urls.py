# pages/urls.py
from django.urls import path
from .views import index
from .views import run

urlpatterns = [
    path('', index, name='home'),
    path('run', run, name='run')
]
