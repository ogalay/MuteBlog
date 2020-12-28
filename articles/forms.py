from .models import Post, Article
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('creator', 'created', 'article')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('created', )


