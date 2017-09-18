# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-12 15:10
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0021_issue_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
