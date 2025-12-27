from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control mb-3 p-3 bg-dark bg-warning text-dark',
                'rows': 8,
                'placeholder': 'What\'s happening?'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control text-light border-secondary mb-3 bg-dark p-2 bg-light inline'
            }),
        }