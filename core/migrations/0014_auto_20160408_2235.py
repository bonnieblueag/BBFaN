# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20160408_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graftedstock',
            name='pot',
            field=models.ForeignKey(null=True, to='core.Pot', blank=True),
        ),
    ]
