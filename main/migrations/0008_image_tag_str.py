# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150108_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tag_str',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
