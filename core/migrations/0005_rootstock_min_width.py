# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160330_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='rootstock',
            name='min_width',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
    ]
