# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_photo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image_url',
        ),
    ]
