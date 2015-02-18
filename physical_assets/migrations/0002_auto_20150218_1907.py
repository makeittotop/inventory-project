# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physical_assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset_detail',
            name='asset_sell_price',
        ),
        migrations.AddField(
            model_name='asset_detail',
            name='asset_sale_price',
            field=models.FloatField(default=None, verbose_name=b'Sale Price'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_computer',
            name='asset_cpu_cores',
            field=models.IntegerField(default=32, max_length=200, verbose_name=b'CPU Cores', choices=[(8, b'Eight'), (16, b'Sixteen'), (32, b'Thirty Two'), (64, b'Sixty Four'), (96, b'Ninety Six')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_computer',
            name='asset_external_nic',
            field=models.CharField(max_length=200, verbose_name=b'External NIC'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_computer',
            name='asset_gfx_card',
            field=models.CharField(default=b'K4000', max_length=200, verbose_name=b'Graphic Card', choices=[(b'K4000', b'K4000'), (b'K5000', b'K5000'), (b'K3000', b'K3000')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_computer',
            name='asset_hard_disk',
            field=models.CharField(default=b'500 GB', max_length=200, verbose_name=b'H.D.D', choices=[(b'250 GB', b'250 GB'), (b'500 GB', b'500 GB'), (b'1 TB', b'1 TB')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_computer',
            name='asset_ram',
            field=models.IntegerField(default=16, max_length=200, verbose_name=b'RAM', choices=[(8, b'Eight'), (16, b'Sixteen'), (32, b'Thirty Two'), (64, b'Sixty Four'), (96, b'Ninety Six')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_category',
            field=models.CharField(max_length=200, verbose_name=b'Category', choices=[(b'work_station', b'Work Station'), (b'server', b'Server'), (b'render_farm', b'Render Farm')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_checkout',
            field=models.CharField(max_length=200, verbose_name=b'In use by'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_condition',
            field=models.CharField(default=b'New', max_length=200, verbose_name=b'Condition', choices=[(b'new', b'New'), (b'old', b'Old'), (b'broken', b'Broken')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_date_of_purchase',
            field=models.DateTimeField(verbose_name=b'Purchase Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_manufacturer',
            field=models.CharField(max_length=200, verbose_name=b'Manufacturer', choices=[(b'dell', b'DELL'), (b'hp', b'HP')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_model',
            field=models.CharField(max_length=200, verbose_name=b'Model', choices=[(b'foo', b'bar'), (b'toop', b'buzz')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_name',
            field=models.CharField(max_length=200, verbose_name=b'Identifier/Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_notes',
            field=models.TextField(verbose_name=b'Notes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_purchase_price',
            field=models.FloatField(default=None, verbose_name=b'Purchase Price'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_detail',
            name='asset_status',
            field=models.CharField(default=b'In Use', max_length=200, verbose_name=b'Current Status', choices=[(b'in_use', b'In Use'), (b'spare', b'Spare')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_purchase_detail',
            name='asset_invoice',
            field=models.CharField(max_length=200, verbose_name=b'Invoice'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_purchase_detail',
            name='asset_lpo',
            field=models.CharField(max_length=200, verbose_name=b'P.O.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='asset_purchase_detail',
            name='asset_supplier',
            field=models.CharField(max_length=200, verbose_name=b'Supplier'),
            preserve_default=True,
        ),
    ]
