# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0002_auto_20150219_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_checkout',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Assignee', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_condition',
            field=models.CharField(max_length=200, verbose_name=b'Condition', choices=[(b'new', b'New'), (b'old', b'Old'), (b'broken', b'Broken'), (b'in-repair', b'In Repair')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_model',
            field=models.CharField(max_length=200, verbose_name=b'Model', choices=[(b'Z820', b'Z820'), (b'Z820', b'Z820'), (b'9010', b'9010')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='asset_cpu_cores',
            field=models.IntegerField(max_length=200, verbose_name=b'CPU Cores', choices=[(4, b'4'), (6, b'6'), (8, b'8'), (16, b'16'), (20, b'20')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='asset_gfx_card',
            field=models.CharField(max_length=200, verbose_name=b'Graphic Card', choices=[(b'Quadro-K4000', b'Quadro K4000'), (b'Quadro-K5000', b'Quadro K5000')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='asset_ram',
            field=models.IntegerField(max_length=200, verbose_name=b'RAM', choices=[(4, b'4'), (16, b'16'), (32, b'32'), (64, b'64')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_detail',
            name='asset_invoice',
            field=models.CharField(max_length=200, verbose_name=b'Invoice Number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_detail',
            name='asset_lpo',
            field=models.CharField(max_length=200, verbose_name=b'P.O. Number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='purchase_detail',
            name='asset_supplier',
            field=models.CharField(max_length=200, verbose_name=b'Supplier Name'),
            preserve_default=True,
        ),
    ]
