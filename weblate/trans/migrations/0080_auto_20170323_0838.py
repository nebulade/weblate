# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0079_autocomponentlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autocomponentlist',
            options={'verbose_name': 'Automatic component list assignment', 'verbose_name_plural': 'Automatic component lists assignments'},
        ),
    ]
