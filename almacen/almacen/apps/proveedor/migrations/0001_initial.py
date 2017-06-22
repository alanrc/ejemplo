# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('genero', models.CharField(choices=[('', 'Selecione Genero '), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=15)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('domicilio', models.CharField(max_length=40)),
                ('empresa', models.CharField(max_length=40)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Proveedor/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['nombre'],
            },
        ),
    ]
