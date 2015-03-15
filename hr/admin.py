from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from hr.models.employee_personal_detail import Employee_Personal_Detail
from hr.models.employee_vacation_detail import Employee_Vacation_Detail, Employee_Vacation

import datetime

# Register your models here.
class Employee_Vacation_Inline(admin.StackedInline):
    model = Employee_Vacation
    extra = 0

class Employee_Personal_Detail_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields' : ['first_name', 'last_name', 'gender', 'country', 'dob', 'personal_email', 'personal_contact_number', \
        'passport_number', 'photo', 'thumb']}),
        ('Official Information', {'fields': ['code', 'official_email', 'designation', 'hire_date', 'end_hire_date', 'department', 'status', 'notes']}),
    ]
    list_display = ('first_name', 'last_name', 'personal_email', 'thumb')
    #list_display = ('name', 'department_cap', 'thumb')
    readonly_fields = ('thumb',)
    search_fields = ['first_name', 'last_name', 'personal_email']

    def first_name(self, obj):
        return "{0}".format(obj.first_name.capitalize())
    first_name.short_description = "First Name"

    def name(self, obj):
        return "{0} {1}".format(obj.first_name.capitalize(), obj.last_name.capitalize())
    name.short_description = "Full Name"

    def department_cap(self, obj):
        return obj.department.capitalize()
    department_cap.short_description = "Department"    

admin.site.register(Employee_Personal_Detail, Employee_Personal_Detail_Admin)

class Employee_Vacation_Detail_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Details', {'fields' : ['employee', 'available_pto', ]}),
        ('Vacations', {'fields' : []}),
    ]
    list_display = ('employee', 'available_pto', 'test')
    readonly_fields = ('available_pto', )
    inlines = [Employee_Vacation_Inline]

    def available_pto(self, inst):
        total_hire_days = datetime.date.today() - inst.employee.hire_date
        total_hire_months = float(total_hire_days.days) / 30
        return "{0:.2f}".format(total_hire_months * 2.5)

    def test(self, inst):
        if len(inst.vacations.all()):
            return "Vacation start date: {0}".format(inst.vacations.all()[0].vacation_start)
        else:
            return "No vacation scheduled."    
        
    available_pto.short_description = 'Available P.T.O.'
    available_pto.allow_tags = True        

admin.site.register(Employee_Vacation_Detail, Employee_Vacation_Detail_Admin)