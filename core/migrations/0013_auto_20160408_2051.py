# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20160406_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='graftedstock',
            name='name_denormalized',
            field=models.CharField(max_length=255, default='Grafted'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seedlingtree',
            name='name_denormalized',
            field=models.CharField(max_length=255, default='Seedling'),
            preserve_default=False,
        ),
    ]
