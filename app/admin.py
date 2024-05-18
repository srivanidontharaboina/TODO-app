from django.contrib import admin

# Register your models here.
from app.models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at')
    search_fields=('task',)
admin.site.register(Task,TaskAdmin)