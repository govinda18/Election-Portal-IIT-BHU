# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-28 20:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election_Portal', '0007_auto_20170928_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='room',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
