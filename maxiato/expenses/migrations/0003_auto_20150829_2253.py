# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_remove_expense_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=255)),
                ('type', models.CharField(default=None, max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=None, max_length=255)),
                ('password', models.CharField(default=None, max_length=255)),
                ('first_name', models.CharField(default=None, max_length=255, blank=True)),
                ('last_name', models.CharField(default=None, max_length=255, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='expense',
            name='city',
            field=models.CharField(default=None, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='country',
            field=models.CharField(default=None, max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateField(default=None, blank=True),
        ),
        migrations.AddField(
            model_name='expense',
            name='reimbursed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(to='expenses.User'),
        ),
        migrations.AddField(
            model_name='expense',
            name='device',
            field=models.ForeignKey(default=None, to='expenses.Device'),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=None, to='expenses.User'),
        ),
    ]
