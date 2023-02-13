from django.contrib import admin
from parler.admin import TranslatableAdmin

from comments.models import Comment
from news.models import News


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class NewsAdmin(TranslatableAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'slug')

admin.site.register(News, NewsAdmin)
