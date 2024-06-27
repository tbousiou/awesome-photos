from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['source_url', 'body']

        labels = {
            'source_url': 'Source Image URL',
            'body': 'Caption'
        }

        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a caption...', 'class': 'font1 text-4xl'}),
        }

class PostEditForm(ModelForm):

    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body' : '',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }