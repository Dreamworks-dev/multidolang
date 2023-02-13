from django.shortcuts import render

from .models import Page
from utils.translation import translate

def index(request):
    translate(request)
    pages = Page.objects.all()
    context = {
        'pages': pages
    }
    return render(request, 'pages/index.html', context)

def detail(request, slug):
    language_code = translate(request)
    page = Page.objects.get(slug=slug)
    comments = []

    for comment in page.comment_set.all():
        if comment.language == language_code:
            comments.append(comment)

    context = {
        'page': page,
        'comments': comments
    }
    return render(request, 'pages/detail.html', context)

