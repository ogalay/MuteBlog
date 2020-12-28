from django.shortcuts import render, redirect
import re
import urllib.request
import requests
from bs4 import BeautifulSoup
from .models import News


# Create your views here.
def index(request):
    site = "https://planetrock.ru/news"

    news_link = urllib.request.urlopen(site)
    soup = BeautifulSoup(news_link, "html.parser")
    news = soup.find_all('h2', {"class": "entry-title"})
    subnews = soup.find_all('div', {"class": "entry-content"})
    dates = soup.find_all('time', {"class": "entry-date"})
    # for n in news:
    #    print(re.findall(r"href=\".*?\"", str(n))[0].replace("href=\"", '').replace("\"", ''))

    mnews = {}

    for i in range(len(news)):
        mnews[re.findall(r"title=\".*?\"", str(news[i]))[0].replace("title=\"", '').replace('"', '')] \
            = [re.findall(r"href=\".*?\"", str(news[i]))[0].replace("href=\"", '').replace("\"", ''),
               re.findall(r"<p>.*?<", str(subnews[i]))[0].replace('<p', '').replace('>', '').replace('<', ''),
               re.findall(r">.*?</time", str(dates[i]))[0].replace(">", '').replace("</time", '')]
        #print(mnews)

    for n in mnews:
        new_news = News()
        new_news.title = n
        new_news.link = mnews[n][0]
        new_news.description = mnews[n][1]
        new_news.posted = mnews[n][2]
        try:
            new_news.validate_unique()
            new_news.save()
        except:
            pass
    all_news = News.objects.all()

    return render(request, 'my_news/news.html', {'all_news': all_news})

