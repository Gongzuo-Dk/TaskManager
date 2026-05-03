from django.contrib import admin
from .models import Category, Priority, Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "priority", "due_date")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass
