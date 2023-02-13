from django.contrib import admin
from parler.admin import TranslatableAdmin

from comments.models import Comment
from pages.models import Page


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PageAdmin(TranslatableAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'slug')

admin.site.register(Page, PageAdmin)
