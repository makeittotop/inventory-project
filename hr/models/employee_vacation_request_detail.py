from django.db import models
from django.utils.html import mark_safe

from hr.models.employee_personal_detail import Employee_Personal_Detail
from hr.models.employee_vacation_detail import Employee_Vacation_Detail   	


class Employee_Vacation_Request_Detail(models.Model):
    #employee_vacation_request = models.OneToOneField(Employee_Vacation_Request)
    employee = models.OneToOneField(Employee_Personal_Detail, primary_key=True)

    def __str__(self):
    	return "{0}".format(employee.first_name)

    class Meta:
    	ordering = ('employee', )
        verbose_name = 'Employee Vacation Request Detail'
        verbose_name_plural = 'Employee Vacation Request Details'


class Employee_Vacation_Request(models.Model):
    vacation_request_choices = (
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
    
    #employee = models.CharField("Name", default="Abhishek Pareek", null=False, blank=False, max_length=200)
    vacation_request_type = models.CharField("Type of vacation", choices=vacation_request_choices, null=False, blank=False, max_length=200)
    vacation_request_start = models.DateField("Start day of vacation", null=False, blank=False);
    vacation_request_end = models.DateField("Last day of vacation", null=False, blank=False);
    vacation_request_note = models.TextField("Description", null=True, blank=True)

    
    vacation_request_approval_choices = (
        (1, 'Approve'),
        (2, 'Deny'),
    )
    vacation_request_approval = models.CharField('Confirmation', choices=vacation_request_approval_choices, blank=False, null=False, max_length=200)
    
    
    employee_vacation_request_detail = models.ForeignKey(Employee_Vacation_Request_Detail, related_name="vacation_requests")

    class Meta:
        verbose_name = 'Employee Vacation Request'
        verbose_name_plural = 'Employee Vacation Requests'        
    
