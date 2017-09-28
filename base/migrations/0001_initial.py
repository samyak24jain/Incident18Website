# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 15:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^[7-9][0-9]*$')])),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Team')),
            ],
        ),
    ]
