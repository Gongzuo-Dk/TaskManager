from django import forms
from .models import Task, Category, Priority

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
    )
    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        required=False,
    )

    class Meta:
        model = Task
        fields = ["title", "content", "category", "priority", "due_date"]