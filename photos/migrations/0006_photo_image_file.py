# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_remove_photo_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(default='404.jpg', upload_to=b''),
            preserve_default=False,
        ),
    ]
