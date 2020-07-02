# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-28 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20200609_0413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'verbose_name': '\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f', 'verbose_name_plural': '\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438'},
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='info',
            name='info_name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u0430'),
        ),
        migrations.AddField(
            model_name='info',
            name='info_name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u0430'),
        ),
        migrations.AddField(
            model_name='listing',
            name='address_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AddField(
            model_name='listing',
            name='address_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AddField(
            model_name='listing',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='listing',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='listing',
            name='city_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
        migrations.AddField(
            model_name='listing',
            name='city_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
        migrations.AddField(
            model_name='listing',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='listing',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='listing',
            name='district_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0420\u0430\u0439\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='listing',
            name='district_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0420\u0430\u0439\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='listing',
            name='region_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='listing',
            name='region_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='listing',
            name='sale_and_rental_en',
            field=models.CharField(blank=True, help_text='\u041f\u0440\u043e\u0434\u0430\u0436\u0430 \u0438\u043b\u0438 \u0430\u0440\u0435\u043d\u0434\u0430', max_length=100, null=True, verbose_name='\u0414\u043b\u044f'),
        ),
        migrations.AddField(
            model_name='listing',
            name='sale_and_rental_ru',
            field=models.CharField(blank=True, help_text='\u041f\u0440\u043e\u0434\u0430\u0436\u0430 \u0438\u043b\u0438 \u0430\u0440\u0435\u043d\u0434\u0430', max_length=100, null=True, verbose_name='\u0414\u043b\u044f'),
        ),
        migrations.AddField(
            model_name='listing',
            name='state_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='listing',
            name='state_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='listing',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='\u0417\u0430\u0433\u0430\u043b\u043e\u0432\u0430\u043a'),
        ),
        migrations.AddField(
            model_name='listing',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='\u0417\u0430\u0433\u0430\u043b\u043e\u0432\u0430\u043a'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(blank=True, default=0, verbose_name='\u0441\u043f\u0430\u043b\u044c\u043d\u0438'),
        ),
    ]