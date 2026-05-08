from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/create/", views.task_create, name="task_create"),
    path("tasks/<int:pk>/edit/", views.task_update, name="task_update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task_delete"),
    path("tasks/<int:pk>/complete/", views.task_toggle_complete, name="task_toggle_complete"),
    path("search/", views.search, name="search"),
    path("today/", views.today, name="today"),
    path("completed/", views.completed, name="completed"),
    path("category/create/", views.category_create, name="category_create"),
    path("category/<int:pk>/edit/", views.category_update, name="category_update"),
    path("category/<int:pk>/delete/", views.category_delete, name="category_delete"),
    path("category/<int:pk>/", views.category_tasks, name="category_tasks"),
    path("category/<int:pk>/pin/", views.category_toggle_pin, name="category_toggle_pin"),
]