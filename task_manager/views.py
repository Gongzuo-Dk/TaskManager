from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from task_manager.forms import TaskForm, CategoryForm
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from task_manager.models import Task, Category, Priority

# Create your views here.

@login_required
def index(request):
    today = timezone.now().date()
    week_ahead = today + timedelta(days=7)

    all_tasks = Task.objects.filter(user=request.user, is_completed=False)

    today_tasks = all_tasks.filter(due_date__date=today)
    next_7_days_tasks = all_tasks.filter(due_date__date__gt=today, due_date__date__lte=week_ahead)
    later_tasks = all_tasks.filter(due_date__date__gt=week_ahead)
    no_date_tasks = all_tasks.filter(due_date__isnull=True)
    completed_tasks = Task.objects.filter(user=request.user, is_completed=True)

    context = {
        "today_tasks": today_tasks,
        "next_7_days_tasks": next_7_days_tasks,
        "later_tasks": later_tasks,
        "no_date_tasks": no_date_tasks,
        "completed_tasks": completed_tasks,
        "today": today,
    }
    return render(request, "task_manager/index.html", context)

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task created successfully!")
            return redirect("index")
    else:
        form = TaskForm(user=request.user)
    
    return render(request, "task_manager/task_create.html", {"form": form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.user != request.user:
        messages.error(request, "You don't have permission to edit this task.")
        return redirect("index")

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect("index")
    else:
        form = TaskForm(instance=task, user=request.user)

    return render(request, "task_manager/task_update.html", {"form": form, "task": task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.user != request.user:
        messages.error(request, "You don't have permission to delete this task.")
        return redirect("index")
    
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task successfully deleted!")
        return redirect("index")
    
    return render(request, "task_manager/task_delete.html", {"task": task})

@login_required
def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.user != request.user:
        messages.error(request, "You don't have permission to do this")
        return redirect("index")
    
    task.is_completed = not task.is_completed
    task.save(update_fields=["is_completed"])
    return redirect("index")

@login_required
def search(request):
    query = request.GET.get("q", "")
    results = []
    error = None

    if query:
        if len(query) > 30:
            error = "Search query cannot exceed 30 characters."
        else:
            results = Task.objects.filter(
                user=request.user
            ).filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(category__name__icontains=query) |
                Q(priority__name__icontains=query)
            ).distinct().order_by("-created_at")

    context = {
        "query": query,
        "results": results,
        "error": error,
    }

    return render(request, "task_manager/search.html", context)

@login_required
def today(request):
    today = timezone.now().date()
    today_tasks = Task.objects.filter(
        user=request.user,
        is_completed=False,
        due_date__date=today
    ).order_by("due_date")

    context = {
        "today_tasks": today_tasks,
        "today": today,
    }
    return render(request, "task_manager/today.html", context)

@login_required
def completed(request):
    completed_tasks = Task.objects.filter(
        user=request.user,
        is_completed=True
    ).order_by("-created_at")

    context = {
        "completed_tasks": completed_tasks,
    }
    return render(request, "task_manager/completed.html", context)

@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, "Category created successfully!")
            return redirect("index")
    else:
        form = CategoryForm()
    
    return render(request, "task_manager/category_create.html", {"form": form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if category.user != request.user:
        messages.error(request, "You don't have permission to edit this category.")
        return redirect("index")

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect("index")
    else:
        form = CategoryForm(instance=category)

    return render(request, "task_manager/category_update.html", {"form": form, "category": category})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if category.user != request.user:
        messages.error(request, "You don't have permission to delete this category.")
        return redirect("index")
    
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category successfully deleted!")
        return redirect("index")
    
    return render(request, "task_manager/category_delete.html", {"category": category})

@login_required
def category_tasks(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if category.user != request.user:
        messages.error(request, "You don't have permission to view this.")
        return redirect("index")
    
    tasks = Task.objects.filter(
        user=request.user,
        category=category,
        is_completed=False
    ).order_by("due_date")

    completed = Task.objects.filter(
        user=request.user,
        category=category,
        is_completed=True
    )

    context = {
        "category": category,
        "tasks": tasks,
        "completed": completed,
    }
    return render(request, "task_manager/category_tasks.html", context)

@login_required
def category_toggle_pin(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if category.user != request.user:
        messages.error(request, "You don't have permission to do this.")
        return redirect("index")

    category.is_pinned = not category.is_pinned
    category.save(update_fields=["is_pinned"])
    return redirect("category_tasks", pk=pk)