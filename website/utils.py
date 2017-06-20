# -*- coding: utf-8 -*-

import json

from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from sorl.thumbnail import get_thumbnail


class AdminThumbnailMixin(object):
    thumbnail_size = "60x60"
    thumbnail_image_field_name = 'image'
    thumbnail_alt_field_name = None

    def _thumb(self, image, size, alt=None):
        attrs = []
        try:
            src = get_thumbnail(image,size, crop='center').url
        except:
            src = ""

        if alt is not None:
            attrs.append('alt="%s"' % alt)

        return mark_safe('<img src="%s" %s />' % (src, " ".join(attrs)))

    def thumbnail(self, obj):
        if self.thumbnail_alt_field_name:
            kwargs['alt'] = getattr(obj, self.thumbnail_alt_field_name)

        return self._thumb(getattr(obj, self.thumbnail_image_field_name), self.thumbnail_size)
    thumbnail.allow_tags = True
    thumbnail.short_description = _('Thumbnail')
