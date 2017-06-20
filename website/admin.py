from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

from website.models import *
from website.utils import AdminThumbnailMixin

class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ["title", "slug"]
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

class ArticleAdmin(admin.ModelAdmin, AdminThumbnailMixin):
    list_display = ["title", "date", "thumbnail"]
    list_filter = ["M2M_category"]
    readonly_fields = ('date',)
    filter_horizontal = ["M2M_category"]
    thumbnail_image_field_name = 'image'
admin.site.register(Article, ArticleAdmin)


### DEFAULT
app = apps.get_app_config('website')
for model in app.get_models():
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
