from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from task_manager.models import Task, Category, Priority

# Create your views here.

@login_required
def index(request):
    all_tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    context = {
        "all_tasks": all_tasks,
    }
    return render(request, "task_manager/index.html", context)