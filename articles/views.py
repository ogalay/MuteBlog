from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse

from .forms import PostForm, ArticleForm
from .models import Article,  Post
from my_news.models import News
# Create your views here.


def index(request):
    articles = Article.objects.all()
    news = News.objects.all()[len(News.objects.all())-4:]
    return render(request, 'articles/index.html', {'articles': articles, 'news': news})


@login_required
def post_reply(request, article_id):
    form = PostForm()
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post()
            post.article = article
            post.body = request.POST['body']
            post.creator = request.user
            post.save()

            return HttpResponseRedirect(reverse('articles:article', args=(article.id,)), RequestContext(request))

    return render(request, 'articles/article.html', {'form': form, 'article': article})


@login_required
def new_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = Article()
            article.title = form.cleaned_data['title']
            article.description = form.cleaned_data['description']
            article.save()
        return HttpResponseRedirect(reverse('articles:index'), RequestContext(request))

    return render(request, 'articles/new_article.html', {'form': form})


def show_article(request, article_id):
    """Listing of posts in an article."""
    posts = Post.objects.filter(article=article_id).order_by("created")
    article = Article.objects.get(pk=article_id)
    return render(request, 'articles/article.html', {'posts': posts, 'article': article})

