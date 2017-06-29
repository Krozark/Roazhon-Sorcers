# -*- coding: utf-8 -*-

import json
import os

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

def file_cleanup(sender, **kwargs):
    for fieldname in sender._meta.get_all_field_names():
        field = sender._meta.get_field(fieldname)
        if isinstance(field, FileField):
            inst = kwargs['instance']
            f = getattr(inst, fieldname)
            m = inst.__class__._default_manager
            if os.path.exists(f.path) \
                and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)}).exclude(pk=inst._get_pk_val()):
                    try:
                        os.remove(f.path)
                    except:
                        pass

