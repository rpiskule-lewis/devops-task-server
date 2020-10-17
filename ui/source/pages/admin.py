from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ['inputs', 'script']
admin.site.register(Task, TaskAdmin)
