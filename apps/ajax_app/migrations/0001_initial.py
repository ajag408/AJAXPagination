# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-02 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('registered_datetime', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
