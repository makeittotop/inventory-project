# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_notes',
            field=models.TextField(null=True, verbose_name=b'Notes', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_detail',
            name='asset_supplier',
            field=models.CharField(max_length=200, verbose_name=b'Supplier'),
            preserve_default=True,
        ),
    ]
