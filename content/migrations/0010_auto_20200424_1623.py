# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-24 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20200423_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image_cover',
            field=models.ImageField(upload_to='media/img'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image_landscape',
            field=models.ImageField(upload_to='media/img'),
        ),
    ]
