# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-15 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appes', '0004_auto_20171115_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfeed',
            name='description',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]
