# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_cpu_cores', models.IntegerField(default=32, max_length=200, verbose_name=b'number of cpu cores', choices=[(8, b'Eight'), (16, b'Sixteen'), (32, b'Thirty Two'), (64, b'Sixty Four'), (96, b'Ninety Six')])),
                ('asset_gfx_card', models.CharField(default=b'K4000', max_length=200, verbose_name=b'types of gfx cards', choices=[(b'K4000', b'K4000'), (b'K5000', b'K5000'), (b'K3000', b'K3000')])),
                ('asset_ram', models.IntegerField(default=16, max_length=200, verbose_name=b'amount of ram', choices=[(8, b'Eight'), (16, b'Sixteen'), (32, b'Thirty Two'), (64, b'Sixty Four'), (96, b'Ninety Six')])),
                ('asset_hard_disk', models.CharField(default=b'500 GB', max_length=200, verbose_name=b'types of hard disks', choices=[(b'250 GB', b'250 GB'), (b'500 GB', b'500 GB'), (b'1 TB', b'1 TB')])),
                ('asset_external_nic', models.CharField(max_length=200, verbose_name=b'type of external nic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asset_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_category', models.CharField(max_length=200, verbose_name=b'category of asset', choices=[(b'work_station', b'Work Station'), (b'server', b'Server'), (b'render_farm', b'Render Farm')])),
                ('asset_manufacturer', models.CharField(max_length=200, verbose_name=b'manufacturer of asset', choices=[(b'dell', b'DELL'), (b'hp', b'HP')])),
                ('asset_model', models.CharField(max_length=200, verbose_name=b'model of asset', choices=[(b'foo', b'bar'), (b'toop', b'buzz')])),
                ('asset_purchase_price', models.FloatField(verbose_name=b'purchase price of asset')),
                ('asset_sell_price', models.FloatField(verbose_name=b'sell price of asset')),
                ('asset_date_of_purchase', models.DateTimeField(verbose_name=b'date of purchase of asset')),
                ('asset_status', models.CharField(default=b'In Use', max_length=200, verbose_name=b'status of asset', choices=[(b'in_use', b'In Use'), (b'spare', b'Spare')])),
                ('asset_condition', models.CharField(default=b'New', max_length=200, verbose_name=b'condition of asset', choices=[(b'new', b'New'), (b'old', b'Old'), (b'broken', b'Broken')])),
                ('asset_checkout', models.CharField(max_length=200, verbose_name=b'checkout of asset')),
                ('asset_notes', models.TextField(verbose_name=b'notes on asset')),
                ('asset_name', models.CharField(max_length=200, verbose_name=b'name of asset')),
                ('asset_computer', models.ForeignKey(to='physical_assets.Asset_Computer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asset_Purchase_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_lpo', models.CharField(max_length=200, verbose_name=b'l.p.o of asset')),
                ('asset_invoice', models.CharField(max_length=200, verbose_name=b'invoice of asset')),
                ('asset_supplier', models.CharField(max_length=200, verbose_name=b'supplier of asset')),
                ('asset_computer', models.ForeignKey(to='physical_assets.Asset_Computer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
