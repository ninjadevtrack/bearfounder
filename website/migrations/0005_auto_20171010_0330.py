# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-10 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import website.profile


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20171010_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='positions',
            field=website.profile.ChoiceArrayField(base_field=models.CharField(choices=[('0', 'Partnership'), ('1', 'Intern'), ('2', 'Part-Time'), ('3', 'Full-Time'), ('4', 'Contract'), ('5', 'Not Looking')], default='0', max_length=1), size=None),
        ),
    ]
