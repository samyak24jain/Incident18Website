# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20170929_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='base.Team'),
        ),
    ]
