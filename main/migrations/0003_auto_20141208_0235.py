# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='address',
            field=models.CharField(default='img_default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='latitude',
            field=models.FloatField(default=37.1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='longitude',
            field=models.FloatField(default=128.1),
            preserve_default=False,
        ),
    ]
