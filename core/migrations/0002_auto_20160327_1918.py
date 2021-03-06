# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeedlingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('parentage', models.CharField(max_length=255)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Species')),
            ],
        ),
        migrations.CreateModel(
            name='SeedlingTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('min_size', models.PositiveIntegerField()),
                ('max_size', models.PositiveIntegerField()),
                ('on_hand', models.PositiveIntegerField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SeedlingInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('city', 'state', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='seedlinginfo',
            unique_together=set([('species', 'name')]),
        ),
    ]
