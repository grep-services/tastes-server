# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_image_dist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='dist',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
    ]
