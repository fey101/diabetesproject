# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-16 12:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0002_auto_20160408_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedExerciseLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('duration', models.DurationField()),
                ('exercise_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_details_persons', to='community.ExerciseRoutines')),
            ],
        ),
        migrations.CreateModel(
            name='DetailedFoodLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('calories_gained', models.DecimalField(decimal_places=3, max_digits=20)),
                ('recommendation', models.CharField(blank=True, max_length=255, null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_persons', to='recipe.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='DetailedSugarLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('sugarLevel', models.IntegerField()),
                ('period', models.CharField(max_length=255)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sugarDetails_log', to='community.SugarLevelDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=10)),
                ('height', models.DecimalField(decimal_places=1, max_digits=10)),
                ('diabetic', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(verbose_name='Date of birth (YYYY-MM-DD)')),
                ('exercise_logs', models.ManyToManyField(through='journal.DetailedExerciseLog', to='community.ExerciseRoutines')),
                ('food_logs', models.ManyToManyField(through='journal.DetailedFoodLog', to='recipe.Recipe')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='journal.Gender')),
                ('health_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.HealthDetails')),
                ('sugar_logs', models.ManyToManyField(through='journal.DetailedSugarLog', to='community.SugarLevelDetails')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='detailedsugarlog',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sugar_log_details', to='journal.Person'),
        ),
        migrations.AddField(
            model_name='detailedfoodlog',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_log_details', to='journal.Person'),
        ),
        migrations.AddField(
            model_name='detailedexerciselog',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_log_details', to='journal.Person'),
        ),
    ]
