# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-10 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_article_titlepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_name', models.CharField(max_length=100, verbose_name='图片名称')),
                ('price', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'prices',
            },
        ),
    ]
