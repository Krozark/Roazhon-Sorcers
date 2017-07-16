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
    list_display = ["title", "date", "created_by", "get_categories", "draft", "get_hit_count", "thumbnail"]
    list_filter = ["M2M_category", "draft", "created_by"]
    readonly_fields = ('created_by',)
    filter_horizontal = ["M2M_category"]
    thumbnail_image_field_name = 'image'

    def get_categories(self, obj):
        return ", ".join([x.title for x in obj.M2M_category.all()])

    def get_hit_count(self, obj):
        return obj.hit_count.hits
    
    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.save()
        form.save_m2m()
        return instance

admin.site.register(Article, ArticleAdmin)

class EventAdmin(admin.ModelAdmin, AdminThumbnailMixin):
    list_display = ["title", "date", "frequency", "thumbnail"]
    thumbnail_image_field_name = 'image'
admin.site.register(Event, EventAdmin)


### DEFAULT
app = apps.get_app_config('website')
for model in app.get_models():
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
