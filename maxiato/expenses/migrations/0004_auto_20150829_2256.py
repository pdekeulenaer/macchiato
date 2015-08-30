# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20150829_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='city',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='country',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
    ]
