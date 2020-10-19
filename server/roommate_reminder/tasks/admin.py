from django.contrib import admin

from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)
