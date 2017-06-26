from datetime import datetime

from django.db import models
from froala_editor.fields import FroalaField
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

class ArticleCategory(models.Model):
    title = models.CharField(_('Title'), max_length=255, unique=True)
    slug = models.SlugField(_("slug"),max_length=140, unique=True)

    def __str__(self):
        return "%s" % self.title


class Article(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    date    = models.DateTimeField(_('Date'), default=datetime.now())
    image  = models.ImageField(upload_to='uploads/realisation',blank=True)    
    M2M_category = models.ManyToManyField(ArticleCategory)
    content = FroalaField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse("website-article", kwargs={"pk": self.pk})
