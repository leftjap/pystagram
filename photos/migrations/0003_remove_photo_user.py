# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
    ]
