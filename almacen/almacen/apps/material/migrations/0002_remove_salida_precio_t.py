# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salida',
            name='precio_t',
        ),
    ]
