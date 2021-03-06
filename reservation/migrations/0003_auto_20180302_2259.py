# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-03 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20180302_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='test@testing.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='phone',
            field=models.CharField(default=8881234567L, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='arrival',
            field=models.DateField(),
        ),
    ]
