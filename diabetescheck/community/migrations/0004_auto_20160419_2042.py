# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-19 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20160419_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqs',
            name='detailed_response_url',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]
