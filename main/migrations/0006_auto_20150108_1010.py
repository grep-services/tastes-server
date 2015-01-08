# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_image_positions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='date',
        ),
        migrations.AddField(
            model_name='image',
            name='datetime',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
