# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141208_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='image',
            name='address',
        ),
        migrations.RemoveField(
            model_name='image',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='image',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.OneToOneField(default=2, to='main.Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='tag',
            field=models.ManyToManyField(to='main.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='origin',
            field=models.ImageField(upload_to=b'origin'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(upload_to=b'thumbnail'),
            preserve_default=True,
        ),
    ]
