from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _


class News(TranslatableModel):

    slug = models.SlugField(
        _('slug'),
        default='',
    )

    translations = TranslatedFields(

        title = models.CharField(
            _('title'),
            max_length=255,
            null=True,
            blank=True
        ),

        body = models.TextField(
            _('body'),
            null=True,
            blank=True,
        )
    )

    def __str__(self):
        return f"{self.title}"
