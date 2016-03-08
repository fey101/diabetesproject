# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-04 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='foodItem_recipes', through='recipe.RecipeFoodItem', to='recipe.FoodItem'),
        ),
    ]