from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from employees.models import Employee

# Register your models here.
class Employee_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields' : ['employee_first_name', 'employee_last_name', 'employee_gender', 'employee_country', 'employee_dob', 'employee_personal_email', 'employee_personal_contact_number', \
        'employee_passport_number', 'employee_photo']}),
        ('Official Information', {'fields': ['employee_code', 'employee_official_email', 'employee_hire_date', 'employee_end_hire_date', 'employee_department', 'employee_status', 'employee_notes']}),
    ]
    list_display = ('employee_first_name', 'employee_last_name', 'employee_personal_email', 'thumb')
    #list_display = ('employee_name', 'employee_department_cap', 'thumb')
    readonly_fields = ('thumb',)
    search_fields = ['employee_first_name', 'employee_last_name', 'employee_personal_email']

    def employee_first_name(self, obj):
        return "{0}".format(obj.employee_first_name.capitalize())
    employee_first_name.short_description = "First Name"

    def employee_name(self, obj):
        return "{0} {1}".format(obj.employee_first_name.capitalize(), obj.employee_last_name.capitalize())
    employee_name.short_description = "Full Name"

    def employee_department_cap(self, obj):
        return obj.employee_department.capitalize()
    employee_department_cap.short_description = "Department"    

admin.site.register(Employee, Employee_Admin)
