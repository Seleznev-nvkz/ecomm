# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(default=0)),
                ('unique_code', models.PositiveSmallIntegerField()),
                ('person_name', models.CharField(max_length=200)),
                ('person_email', models.EmailField(max_length=254)),
                ('person_phone', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('New', 'New'), ('In process', 'In process'), ('Ready to deliver', 'Ready to deliver'), ('Delivering', 'Delivering'), ('Delivered', 'Delivered'), ('Suspended', 'Suspended'), ('Cancelled', 'Cancelled')], default='New', max_length=2)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appshop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('is_enabled', models.BooleanField()),
                ('small_photo', models.ImageField(upload_to='')),
                ('big_photo', models.ImageField(upload_to='')),
                ('is_featured', models.BooleanField()),
                ('is_really_hot', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appshop.Category')),
            ],
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appshop.Product'),
        ),
    ]
