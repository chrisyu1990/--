# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hac', '0005_auto_20160217_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendee',
            old_name='corpId',
            new_name='ID',
        ),
    ]
