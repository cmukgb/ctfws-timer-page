# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171029_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuffcount',
            name='blue_belts',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='blue_potions',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='blue_wands',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='green_belts',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='green_potions',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='green_wands',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_alarm',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_belts',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_flags',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_gotcha',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_jail',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_potions',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_recharge',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_wands',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='red_yukko',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='white_belts',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='white_potions',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='white_wands',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='yellow_alarm',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='yellow_flags',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='yellow_gotcha',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='yellow_jail',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='yellow_recharge',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='stuffcount',
            name='yellow_yukko',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
