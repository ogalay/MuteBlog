from django.db import models


class News(models.Model):
    title = models.TextField('Название', max_length=1000, unique=True)
    description = models.TextField('Описание', max_length=2000)
    link = models.CharField('Ссылка', max_length=200)
    posted = models.CharField('Выложена', max_length=50)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


