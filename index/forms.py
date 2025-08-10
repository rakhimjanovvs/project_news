from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, News


# готовая форма с изменениеми
class RegForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Форма для публикации новостей
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'main_content', 'news_category']


# Форма для комментарий
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Напишите комментарий ...'})
        }