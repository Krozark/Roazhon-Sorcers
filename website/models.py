from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_delete
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField

from froala_editor.fields import FroalaField
from hitcount.models import HitCountMixin, HitCount
from website.utils import file_cleanup


class ArticleCategory(models.Model):
    title = models.CharField(_('Title'), max_length=255, unique=True)
    slug = models.SlugField(_("slug"),max_length=140, unique=True)
    
    class Meta:
        ordering = ["title"]

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse("website-home")+"?category="+self.slug


class Article(models.Model, HitCountMixin):
    STATUS_DRAFT = 0
    STATUS_FINISHED = 1
    STATUS_HIDDEN = 2
    STATUS_ASK_FOR_REVIEW = 3
    STATUS = [
            (STATUS_DRAFT, _("Draft")),
            (STATUS_FINISHED, _("Finished")),
            (STATUS_ASK_FOR_REVIEW, _("Ask for review")),
            (STATUS_HIDDEN, _("Hidden"))
            ]


    title              = models.CharField(_('Title'), max_length=255)
    creation_date      = models.DateTimeField(_('Creation date'), default=datetime.now())
    publishing_date    = models.DateTimeField(_('Publication date'), default=datetime.now(), help_text= _("This date specify the minimal date require to see the article"))
    status             = models.IntegerField(_("Status"), default=STATUS_DRAFT, help_text=_("The post status. Will apear in the website in Finished state only"), choices=STATUS)
    created_by         = models.ForeignKey(User)
    image              = ResizedImageField(upload_to='uploads/article',blank=True, size=[1920, 1080], crop=['middle', 'center'], quality=75)
    M2M_category       = models.ManyToManyField(ArticleCategory)
    content            = FroalaField(help_text=_("You can use http://www.strawpoll.me/ to create polls"))

    hit_count_generic  = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ["-publishing_date"]

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse("website-article", kwargs={"pk": self.pk})

    @staticmethod
    def get_queryset(category=None):
        now = datetime.now()
        queryset = Article.objects.filter(status=Article.STATUS_FINISHED, publishing_date__lte=now)
        if category:
            queryset = queryset.filter(M2M_category__slug=category)
        return queryset
post_delete.connect(file_cleanup, sender=Article, dispatch_uid="Article.file_cleanup")

class Event(models.Model):
    title = models.CharField(_('Title'), max_length=255)

    time = models.TimeField(_('Time'))
    date = models.DateField(_('Date'), blank=True, null=True, help_text=_("Use this field or frequency, but not both"))
    frequency = models.CharField(_('frequence'), max_length=255, blank=True, help_text=_("Use thi field or date but not both"))

    place   = models.CharField(_('Place'), max_length=255, blank=True)
    image   = ResizedImageField(upload_to='uploads/event', blank=False, size=[350, 300], quality=75)
    url     = models.URLField("url", blank=True, null=True)
    content = FroalaField(blank=True)

    class Meta:
        ordering = ["date", "time", "title"]

    def __str__(self):
        return "%s" % self.title

    @staticmethod
    def get_next_events(limit=4, day_limit=7):
        return Event.objects.filter(date=None) | Event.objects.filter(date__gte= datetime.now() - timedelta(days=day_limit))[:limit]

