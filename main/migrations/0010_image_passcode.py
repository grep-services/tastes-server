# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_image_orientations'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='passcode',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
