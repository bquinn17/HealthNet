# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-02 14:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('uses', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 15, 6, 4, 733929), verbose_name='End Time'),
        ),
        migrations.RemoveField(
            model_name='patient',
            name='prescriptions',
        ),
        migrations.AddField(
            model_name='patient',
            name='prescriptions',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='health.Prescription'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='temp_check_in_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 14, 6, 4, 727924)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='temp_check_out_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 14, 6, 4, 727924)),
        ),
    ]
