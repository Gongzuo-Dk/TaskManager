from django.shortcuts import render
from task_manager.models import Task, Category, Priority

# Create your views here.

def index(request):
    all_tasks = Task.objects.order_by("-created_at")
    context = {
        "all_tasks": all_tasks,
    }

    return render(request, "task_manager/index.html", context)