# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150108_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='datetime',
            new_name='time',
        ),
    ]
