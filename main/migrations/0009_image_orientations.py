# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_image_tag_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='orientations',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
