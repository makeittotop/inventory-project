from django.db import models
from django.utils.html import mark_safe

from hr.models.employee_personal_detail import Employee_Personal_Detail

class Employee_Vacation_Detail(models.Model):
    employee = models.OneToOneField(Employee_Personal_Detail, primary_key=True)

    def available_pto(self):
        return "25"
	available_pto.short_description = 'Available P.T.O.'
	available_pto.allow_tags = True

    def __str__(self):
    	return "{0}".format(self.employee.first_name)
