# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-02 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20200502_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='land_area',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c \u0443\u0447\u0430\u0441\u0442\u043a\u0430'),
        ),
    ]
