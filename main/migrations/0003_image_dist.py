# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141212_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='dist',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
    ]
