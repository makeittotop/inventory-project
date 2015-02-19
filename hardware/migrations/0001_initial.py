# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_category', models.CharField(max_length=200, verbose_name=b'Category', choices=[(b'work_station', b'Work Station'), (b'server', b'Server'), (b'render_farm', b'Render Farm')])),
                ('asset_manufacturer', models.CharField(max_length=200, verbose_name=b'Manufacturer', choices=[(b'dell', b'DELL'), (b'hp', b'HP')])),
                ('asset_model', models.CharField(max_length=200, verbose_name=b'Model', choices=[(b'foo', b'bar'), (b'toop', b'buzz')])),
                ('asset_purchase_price', models.FloatField(null=True, verbose_name=b'Purchase Price', blank=True)),
                ('asset_sale_price', models.FloatField(null=True, verbose_name=b'Sale Price', blank=True)),
                ('asset_date_of_purchase', models.DateTimeField(null=True, verbose_name=b'Purchase Date', blank=True)),
                ('asset_status', models.CharField(max_length=200, verbose_name=b'Current Status', choices=[(b'in_use', b'In Use'), (b'spare', b'Spare')])),
                ('asset_condition', models.CharField(max_length=200, verbose_name=b'Condition', choices=[(b'new', b'New'), (b'old', b'Old'), (b'broken', b'Broken')])),
                ('asset_checkout', models.CharField(max_length=200, null=True, verbose_name=b'Used by', blank=True)),
                ('asset_notes', models.TextField(null=True, verbose_name=b'Notes', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_cpu_cores', models.IntegerField(max_length=200, verbose_name=b'CPU Cores', choices=[(8, b'8'), (16, b'16'), (32, b'32'), (64, b'64'), (96, b'96')])),
                ('asset_gfx_card', models.CharField(max_length=200, verbose_name=b'Graphic Card', choices=[(b'K4000', b'K4000'), (b'K5000', b'K5000'), (b'K3000', b'K3000')])),
                ('asset_ram', models.IntegerField(max_length=200, verbose_name=b'RAM', choices=[(8, b'8'), (16, b'16'), (32, b'32'), (64, b'64'), (96, b'96')])),
                ('asset_hard_disk', models.CharField(max_length=200, verbose_name=b'H.D.D', choices=[(b'250 GB', b'250 GB'), (b'500 GB', b'500 GB'), (b'1 TB', b'1 TB')])),
                ('asset_external_nic', models.CharField(max_length=200, verbose_name=b'External NIC', choices=[(b'10G', b'10G')])),
                ('asset_serial_number', models.CharField(max_length=200, verbose_name=b'Serial Number')),
                ('asset_name', models.CharField(max_length=200, verbose_name=b'Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_lpo', models.CharField(max_length=200, verbose_name=b'P.O.')),
                ('asset_invoice', models.CharField(max_length=200, verbose_name=b'Invoice')),
                ('asset_supplier', models.CharField(max_length=200, verbose_name=b'Supplier')),
                ('computer', models.OneToOneField(to='hardware.Computer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='asset_detail',
            name='computer',
            field=models.OneToOneField(to='hardware.Computer'),
            preserve_default=True,
        ),
    ]
