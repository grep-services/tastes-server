# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origin', models.ImageField(upload_to=b'origin')),
                ('thumbnail', models.ImageField(upload_to=b'thumbnail')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='tag',
            field=models.ManyToManyField(to='main.Tag', null=True),
            preserve_default=True,
        ),
    ]
