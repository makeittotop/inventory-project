# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset_detail',
            name='asset_name',
        ),
    ]
