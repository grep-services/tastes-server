# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20141222_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='positions',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
