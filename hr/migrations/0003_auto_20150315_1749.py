# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_remove_employee_vacation_detail_employee_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Vacation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vacation_type', models.CharField(max_length=200, verbose_name=b'Type of vacation', choices=[(b'AL', b'Annual Leave'), (b'BUS', b'Business Trip'), (b'COL', b'Compassionate Leave'), (b'COM', b'Compensatory Leave'), (b'EID', b'EID Holidays'), (b'PAT', b'Paternity Leave'), (b'SAL', b'Special approved Leave with pay'), (b'SL', b'Sick Leave'), (b'UL', b'Unpaid Leave deducted from Salary'), (b'UPL', b'Unpaid Leave')])),
                ('vacation_start', models.DateField(verbose_name=b'Start day of vacation')),
                ('vacation_end', models.DateField(verbose_name=b'End day of vacation')),
                ('vacation_note', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('employee_vacation_detail', models.ForeignKey(to='hr.Employee_Vacation_Detail')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee_vacation_detail',
            name='employee_hire_date',
            field=models.DateField(default=b'2013-07-07', verbose_name=b'Hire Date'),
            preserve_default=True,
        ),
    ]
