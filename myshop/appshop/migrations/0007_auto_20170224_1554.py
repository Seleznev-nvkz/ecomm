# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appshop', '0006_auto_20170224_0515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='big_photo',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slider_photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='small_photo',
        ),
    ]
