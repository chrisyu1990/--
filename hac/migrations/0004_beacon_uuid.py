# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hac', '0003_beacon_macaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='uuid',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
