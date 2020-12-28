from django.conf import settings
from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=10000)
    created = models.DateTimeField('Создан', auto_now=True)

    def num_post(self):
        num_posts = Post.objects.filter(article=self).count()
        return num_posts

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Post(models.Model):
    created = models.DateTimeField('Создан', auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField('Текст сообщения', max_length=1000)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
