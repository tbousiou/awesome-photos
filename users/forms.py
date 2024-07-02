from .models import Profile
from django import forms
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'displayname', 'bio', 'location']

        widgets = {
            'avatar': forms.FileInput(),
            'bio' : forms.Textarea(attrs={'rows':3})
        }