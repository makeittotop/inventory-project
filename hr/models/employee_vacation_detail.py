from django.db import models
from django.utils.html import mark_safe

from hr.models.employee_personal_detail import Employee_Personal_Detail

class Employee_Vacation_Detail(models.Model):
    employee = models.OneToOneField(Employee_Personal_Detail, primary_key=True)
    employee_hire_date = models.DateField("Hire Date", default="2013-07-07", blank=False, null=False)

    def __str__(self):
    	return "{0}".format(self.employee.first_name.capitalize())

class Employee_Vacation(models.Model):
    vacation_choices = (
        ('AL', 'Annual Leave'),
        ('BUS', 'Business Trip'),
        ('COL', 'Compassionate Leave'),
        ('COM', 'Compensatory Leave'),
        ('EID', 'EID Holidays'),
        ('PAT', 'Paternity Leave'),
        ('SAL', 'Special approved Leave with pay'),
        ('SL', 'Sick Leave'),
        ('UL', 'Unpaid Leave deducted from Salary'),
        ('UPL', 'Unpaid Leave'),
	)
    vacation_type = models.CharField("Type of vacation", choices=vacation_choices, null=False, blank=False, max_length=200)
    vacation_start = models.DateField("Start day of vacation", null=False, blank=False);
    vacation_end = models.DateField("End day of vacation", null=False, blank=False);
    vacation_note = models.TextField("Description", null=True, blank=True)
    
    employee_vacation_detail = models.ForeignKey(Employee_Vacation_Detail)
