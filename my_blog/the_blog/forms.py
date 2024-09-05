from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'author', 'body', 'category')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Write here', 'style': 'width: 400px;'}),
            'author' : forms.Select(attrs={'class' : 'form-control', 'style': 'width: 150px;'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Write here'}),
            'category' : forms.Select(attrs={'class' : 'form-control', 'style': 'width: 150px;'}),
        }