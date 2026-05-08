from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar"]

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        if avatar and avatar.size > 2 * 1024 * 1024:
            raise forms.ValidationError("Image size must be under 2MB.")
        return avatar