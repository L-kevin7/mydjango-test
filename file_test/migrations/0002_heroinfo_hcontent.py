# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroinfo',
            name='hcontent',
            field=models.CharField(max_length=100, null=True, verbose_name='绝招'),
        ),
    ]
