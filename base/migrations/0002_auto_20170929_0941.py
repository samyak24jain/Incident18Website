# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='team',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]