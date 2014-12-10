# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20141209_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Location'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='tag',
            field=models.ManyToManyField(to='main.Tag', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
