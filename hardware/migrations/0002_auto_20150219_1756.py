# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_detail',
            name='asset_lpo',
            field=models.CharField(default=None, max_length=200, verbose_name=b'P.O.'),
            preserve_default=True,
        ),
    ]
