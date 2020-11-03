from django.db import models
from wagtail.core.models import Page

# other imports
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.


class ProjectIndexPage(Page):
    subtitle = models.CharField(max_length=255)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body')
    ]
