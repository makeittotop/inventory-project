# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0002_auto_20150219_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_detail',
            name='computer',
            field=models.OneToOneField(to='hardware.Computer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_detail',
            name='computer',
            field=models.OneToOneField(to='hardware.Computer'),
            preserve_default=True,
        ),
    ]
