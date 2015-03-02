# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0004_auto_20150225_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_date_of_purchase',
            field=models.DateField(null=True, verbose_name=b'Purchase Date', blank=True),
            preserve_default=True,
        ),
    ]
