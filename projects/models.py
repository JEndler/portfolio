from django.db import models
from wagtail.core.models import Page

# other imports
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from wagtailcodeblock.blocks import CodeBlock

# Create your models here.

class ProjectPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ProjectPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class ProjectPage(Page):
    subtitle = models.CharField(max_length=255)
    body = body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('code', CodeBlock())
    ])
    button_text = models.CharField(max_length=30, default="Visit Project")
    button_href = models.CharField(
        max_length=255,
        default="jakobendler.eu/404"
    )
    github_href = models.CharField(max_length=255, null=True)
    tags = ClusterTaggableManager(through=ProjectPageTag, blank=True)
    big_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('body'),
        FieldPanel('tags'),
        FieldPanel('big_image'),
        FieldPanel('button_text'),
        FieldPanel('button_href'),
        FieldPanel('github_href')
    ]
