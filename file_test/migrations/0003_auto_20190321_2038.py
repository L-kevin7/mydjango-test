# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_test', '0002_heroinfo_hcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='hsex',
            field=models.SmallIntegerField(choices=[(0, 'woman'), (1, 'man')], default=0, verbose_name='性别'),
        ),
    ]