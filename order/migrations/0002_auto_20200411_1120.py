# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-11 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='text',
            field=models.CharField(max_length=200, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f'),
        ),
    ]
