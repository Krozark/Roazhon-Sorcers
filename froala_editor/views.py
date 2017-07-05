import json
import os
import math
import random
import string


# from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils.translation import ugettext_lazy as _

from PIL import Image


def resize_image(the_file):
    max_width, max_height = getattr(settings, 'DJANGORESIZED_DEFAULT_SIZE', (1920, 1080))
    image = Image.open(the_file)
    width, height = image.size
    ratio = min((max_width/width, max_height/height))
    if ratio < 1:
        width = math.floor(width*ratio)
        height = math.floor(height*ratio)
        image = image.resize((width, height), Image.ANTIALIAS)
    return image



def image_upload(request):
    if 'file' in request.FILES:
        the_file = request.FILES['file']
        allowed_types = ['image/jpeg', 'image/jpg', 'image/pjpeg', 'image/x-png', 'image/png', 'image/gif']
        if not the_file.content_type in allowed_types:
            return HttpResponse(json.dumps({'error': _('You can only upload images.')}),
                                content_type="application/json")
        # Other data on the request.FILES dictionary:
        # filesize = len(file['content'])
        # filetype = file['content-type']
        upload_to = getattr(settings, 'FROALA_UPLOAD_PATH', 'uploads/froala_editor/images/')

        image = resize_image(the_file)
        path = os.path.join(upload_to, ''.join([random.choice(string.ascii_lowercase) for i in range(32)]) + ".jpg")
        full_path = os.path.join(settings.MEDIA_ROOT, path)

        image.save(full_path, format='JPEG')
        link = default_storage.url(path)

        return HttpResponse(json.dumps({'link': link}), content_type="application/json")


def file_upload(request):
    if 'file' in request.FILES:
        the_file = request.FILES['file']
        upload_to = getattr(settings, 'FROALA_UPLOAD_PATH', 'uploads/froala_editor/files/')
        path = default_storage.save(os.path.join(upload_to, the_file.name), the_file)
        link = default_storage.url(path)
        return HttpResponse(json.dumps({'link': link}), content_type="application/json")
