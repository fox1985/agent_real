# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-19 13:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0435\u043a\u043e\u0432\u0430\u0442\u044c')),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Galary_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galary_image', models.ImageField(blank=True, upload_to='photos-home/%Y/%m/%d/', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
            ],
            options={
                'db_table': 'galary_image',
                'verbose_name': '\u0413\u0430\u043b\u0438\u0440\u0435\u044f',
                'verbose_name_plural': '\u0413\u0430\u043b\u0438\u0440\u0435\u0438',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_name', models.CharField(max_length=100, verbose_name='\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u0430')),
            ],
            options={
                'verbose_name': '\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u0430',
                'verbose_name_plural': '\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u0430',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='\u0417\u0430\u0433\u0430\u043b\u043e\u0432\u0430\u043a')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('district', models.CharField(blank=True, max_length=200, verbose_name='\u0420\u0430\u0439\u043e\u043d')),
                ('region', models.CharField(blank=True, max_length=100, verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d')),
                ('rooms', models.IntegerField(default=0, verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('state', models.CharField(blank=True, max_length=100, verbose_name='\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435')),
                ('description', models.TextField(blank=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('price', models.CharField(max_length=200, verbose_name='\u0446\u0435\u043d\u0430')),
                ('bedrooms', models.IntegerField(blank=True, verbose_name='\u0441\u043f\u0430\u043b\u044c\u043d\u0438')),
                ('bathrooms', models.IntegerField(blank=True, default=0, verbose_name='\u0432\u0430\u043d\u043d\u044b\u0435 \u043a\u043e\u043c\u043d\u0430\u0442\u044b')),
                ('garage', models.IntegerField(default=0, verbose_name='\u0433\u0430\u0440\u0430\u0436')),
                ('sqft', models.IntegerField(default=0, verbose_name='\u041a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0435 \u043c\u0435\u0442\u0440\u044b')),
                ('land_area', models.CharField(blank=True, max_length=200, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c \u0443\u0447\u0430\u0441\u0442\u043a\u0430')),
                ('terrace_area', models.IntegerField(default=0, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c \u0442\u0435\u0440\u0440\u0430\u0441\u044b')),
                ('lot_size', models.CharField(max_length=200, verbose_name='\u043d\u043e\u043c\u0435\u0440 ID')),
                ('vid_name', models.CharField(blank=True, help_text='\u0412\u0438\u0434 \u043d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438 \u043d\u0430 \u043f\u0440\u0438\u043c\u0435\u0440 \u043d\u043e\u0432\u043e\u0441\u0442\u0440\u043e\u0439', max_length=100, verbose_name='\u0432\u0438\u0434')),
                ('tip_name', models.CharField(blank=True, help_text='\u0422\u0438\u043f \u043d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u044c', max_length=100, verbose_name='\u0422\u0438\u043f')),
                ('sale_and_rental', models.CharField(blank=True, help_text='\u041f\u0440\u043e\u0434\u0430\u0436\u0430 \u0438\u043b\u0438 \u0430\u0440\u0435\u043d\u0434\u0430', max_length=100, verbose_name='\u0414\u043b\u044f')),
                ('from_the_sea', models.IntegerField(blank=True, default=0, help_text='\u0435\u0441\u043b\u0438 \u043d\u0435 \u043d\u0443\u0436\u043d\u043e \u043e\u0442\u043c\u0435\u0447\u0430\u0442\u044c \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043e\u0442 \u043c\u043e\u0440\u044f \u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 <<\u043d\u043e\u043b\u044c>>', verbose_name='\u043e\u0442 \u043c\u043e\u0440\u044f')),
                ('photo_main', models.ImageField(upload_to='photos-home/%Y/%m/%d/', verbose_name='\u043a\u0430\u0440\u0442\u043e\u0447\u0442\u043a\u0430 \u0442\u043e\u0432\u0430\u0440\u0430')),
                ('is_published', models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('page_info', models.ManyToManyField(blank=True, help_text='\u0427\u0442\u043e \u0435\u0441\u0442\u044c \u0432 \u0434\u043e\u043c\u0435', to='listings.Info', verbose_name='\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u0430')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
            options={
                'db_table': 'listing',
                'verbose_name': '\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438',
            },
        ),
        migrations.AddField(
            model_name='galary_image',
            name='Listing_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.Listing'),
        ),
    ]
