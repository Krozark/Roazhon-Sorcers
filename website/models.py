from datetime import datetime

from django.db import models
from django.db.models.signals import post_delete
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

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
    created_by = models.ForeignKey(User)
    image  = ResizedImageField(upload_to='uploads/article',blank=True, size=[1920, 1080], crop=['middle', 'center'], quality=75)
    M2M_category = models.ManyToManyField(ArticleCategory)
    draft = models.BooleanField(_("Draft"), default=True, help_text=_("The post will no apear in the website in draft state"))
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

    time = models.TimeField(_('Time'))
    date = models.DateField(_('Date'), blank=True, null=True, help_text=_("Use this field or frequency, but not both"))
    frequency = models.CharField(_('frequence'), max_length=255, blank=True, help_text=_("Use thi field or date but not both"))

    place = models.CharField(_('Place'), max_length=255, blank=True)
    image  = ResizedImageField(upload_to='uploads/event', blank=True, size=[350, 300], quality=75)
    content = FroalaField(blank=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return "%s" % self.title

