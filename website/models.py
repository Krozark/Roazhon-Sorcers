from datetime import datetime

from django.db import models
from django.db.models.signals import post_delete
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from froala_editor.fields import FroalaField
from django_resized import ResizedImageField

from website.utils import file_cleanup



class ArticleCategory(models.Model):
    title = models.CharField(_('Title'), max_length=255, unique=True)
    slug = models.SlugField(_("slug"),max_length=140, unique=True)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse("website-home")+"?category="+self.slug


class Article(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    date    = models.DateTimeField(_('Date'), default=datetime.now())
    image  = ResizedImageField(upload_to='uploads/article',blank=True, size=[1920, 1080], crop=['middle', 'center'], quality=75)
    M2M_category = models.ManyToManyField(ArticleCategory)
    content = FroalaField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse("website-article", kwargs={"pk": self.pk})
post_delete.connect(file_cleanup, sender=Article, dispatch_uid="Article.file_cleanup")

class Event(models.Model):
    title = models.CharField(_('Title'), max_length=255)

    date = models.DateField(_('Date'), blank=True, null=True)
    time = models.TimeField(_('Time'))
    frequency = models.CharField(_('frequence'), max_length=255, blank=True)

    place = models.CharField(_('Place'), max_length=255, blank=True)
    image  = ResizedImageField(upload_to='uploads/article',blank=True, size=[350, 300], crop=['middle', 'center'], quality=75)
    content = FroalaField(blank=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return "%s" % self.title

