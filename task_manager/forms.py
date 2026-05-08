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
        queryset=Category.objects.none(),
        required=False,
    )
    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        required=False,
    )

    class Meta:
        model = Task
        fields = ["title", "content", "category", "priority", "due_date"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["category"].queryset = Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):
    is_pinned = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "checkboxCategory"}),
    )

    class Meta:
        model = Category
        fields = ["name", "is_pinned"]