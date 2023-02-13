from django.db import models
from django.utils.translation import gettext_lazy as _

from news.models import News
from pages.models import Page


class Comment(models.Model):
    
    class Language(models.TextChoices):
        English = 'en'
        Deutch = 'de',
        French = 'fr'
    
    language = models.CharField(
        _('language'),
        choices=Language.choices,
        default=Language.English,
        max_length=10
    )

    body = models.TextField(
        _('body'),
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.body}-{self.language}"