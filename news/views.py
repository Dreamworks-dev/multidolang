from django.shortcuts import render

from .models import News
from utils.translation import translate

def index(request):
    translate(request)
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/index.html', context)

def detail(request, slug):
    language_code = translate(request)
    news = News.objects.get(slug=slug)
    comments = []

    for comment in news.comment_set.all():
        if comment.language == language_code:
            comments.append(comment)

    context = {
        'news': news,
        'comments': comments
    }
    return render(request, 'news/detail.html', context)

