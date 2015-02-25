# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0003_auto_20150225_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_model',
            field=models.CharField(max_length=200, verbose_name=b'Model', choices=[(b'T360', b'T360'), (b'Z420', b'Z420'), (b'Z820', b'Z820'), (b'9010', b'9010')]),
            preserve_default=True,
        ),
    ]
