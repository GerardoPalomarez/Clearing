# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-11 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subestadosclearing',
            name='subestado_clearing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subestado_estado', to='catalogos.EstadoClearing'),
        ),
    ]
