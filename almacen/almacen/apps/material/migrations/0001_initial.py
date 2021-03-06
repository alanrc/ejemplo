# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Almacen',
                'verbose_name_plural': 'Almacenes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_u', models.DecimalField(decimal_places=2, max_digits=7)),
                ('precio_t', models.DecimalField(decimal_places=2, max_digits=7)),
                ('num_factura', models.CharField(max_length=10, unique=True)),
                ('serie', models.CharField(blank=True, max_length=15, null=True)),
                ('codigo', models.CharField(blank=True, max_length=15, null=True)),
                ('objeto', models.TextField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('fecha_i', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.Funcionario')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
                'ordering': ['-fecha_i'],
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('stock_actual', models.PositiveIntegerField(default='0', verbose_name='Stock Actual')),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Almacen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Marca')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Proveedor')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_t', models.DecimalField(decimal_places=2, max_digits=7)),
                ('objeto', models.TextField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.Funcionario')),
                ('ingreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Ingreso')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Material')),
            ],
            options={
                'verbose_name': 'Salida',
                'verbose_name_plural': 'Salidas',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidad de Medidas',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='material',
            name='unidad_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.UnidadMedida'),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Material'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Ingreso'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='salida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Salida'),
        ),
    ]
