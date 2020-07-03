from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    def clean_text(self):
        if self.cleaned_data['text'] is None:
            raise forms.ValidationError(
                    'Пожалуйста, заполните поле "text"',
                    params={'value': self.cleaned_data['text']},
            )
        return self.cleaned_data['text']

    class Meta:
        model = Post
        fields = ['text', 'group']
