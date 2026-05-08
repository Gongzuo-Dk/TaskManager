from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=30)
    is_pinned = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    

class Priority(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name
    
  
class Task(models.Model):
    category = models.ForeignKey(Category, related_name="tasks", on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.ForeignKey(Priority, related_name="tasks", on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        if len(self.title) > 35:
            return self.title[:35] + "..."
        return self.title
