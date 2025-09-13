from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserCreationForm(forms.Form):
    email = forms.forms.EmailField()
    