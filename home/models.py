from django.db import models

from wagtail.core.models import Page

# other imports
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    headline = models.CharField(max_length=255, default='Jakob Endler')
    subheadline = models.CharField(max_length=255, default='Subheadline')
    about_me_text = RichTextField(blank=True)
    get_in_touch_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        FieldPanel('subheadline'),
        FieldPanel('about_me_text'),
        FieldPanel('get_in_touch_text')
    ]
