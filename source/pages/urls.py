# pages/urls.py
from django.urls import path
from .views import folders
from .views import scripts
from .views import tasks

urlpatterns = [
    path('', folders, name='folders'),
    path('v1/folders', folders, name='folders'),
    path('v1/scripts', scripts, name='scripts'),
    path('v1/tasks', tasks, name='tasks'),
]
