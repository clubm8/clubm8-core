# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubm8core', '0004_auto_20160917_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occurrence',
            name='plan',
        ),
        migrations.AddField(
            model_name='plan',
            name='occurence',
            field=models.ManyToManyField(null=True, to='clubm8core.Occurrence'),
        ),
    ]