# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubm8core', '0005_auto_20160917_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='occurence',
            field=models.ManyToManyField(to='clubm8core.Occurrence'),
        ),
    ]
