from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/create/", views.task_create, name="task_create"),
    path("tasks/<int:pk>/edit/", views.task_update, name="task_update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task_delete"),
    path("tasks/<int:pk>/complete/", views.task_toggle_complete, name="task_toggle_complete"),
]