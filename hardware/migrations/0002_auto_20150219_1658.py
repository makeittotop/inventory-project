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
            name='computer',
            field=models.ForeignKey(to='hardware.Computer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_detail',
            name='computer',
            field=models.ForeignKey(to='hardware.Computer'),
            preserve_default=True,
        ),
    ]
