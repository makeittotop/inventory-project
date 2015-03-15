# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Personal_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name=b'Last Name')),
                ('gender', models.SmallIntegerField(verbose_name=b'Gender', choices=[(1, b'Male'), (2, b'Female')])),
                ('country', models.CharField(max_length=200, null=True, verbose_name=b'Home Country', blank=True)),
                ('dob', models.DateField(verbose_name=b'Date of Birth', blank=True)),
                ('personal_email', models.EmailField(max_length=200, verbose_name=b'Personal Email')),
                ('personal_contact_number', models.CharField(max_length=200, verbose_name=b'Contact Number')),
                ('passport_number', models.CharField(max_length=200, verbose_name=b'Passport Number')),
                ('photo', models.ImageField(upload_to=b'photos', null=True, verbose_name=b'Employee Photo', blank=True)),
                ('code', models.CharField(max_length=200, verbose_name=b'Employee Code')),
                ('hire_date', models.DateField(verbose_name=b'Hire Date')),
                ('end_hire_date', models.DateField(null=True, verbose_name=b'End Hire Date', blank=True)),
                ('department', models.CharField(max_length=200, verbose_name=b'Department', choices=[(b'animation', b'Animation'), (b'rigging', b'Rigging'), (b'lighting', b'Lighting'), (b'compositing', b'Compositing'), (b'pipeline', b'Pipeline'), (b'information_technology', b'I.T.'), (b'human_resources', b'H.R.')])),
                ('status', models.CharField(max_length=200, verbose_name=b'Status', choices=[(b'active', b'Active'), (b'inactive', b'Inactive')])),
                ('official_email', models.EmailField(max_length=200, null=True, verbose_name=b'Official Email')),
                ('designation', models.CharField(max_length=200, verbose_name=b'Designation')),
                ('notes', models.TextField(null=True, verbose_name=b'Notes', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee_Vacation_Detail',
            fields=[
                ('employee', models.OneToOneField(primary_key=True, serialize=False, to='hr.Employee_Personal_Detail')),
                ('employee_name', models.CharField(max_length=200, verbose_name=b'Employee', choices=[(b'foo', b'foo'), (b'faa', b'boo'), (b'bar', b'burr')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
