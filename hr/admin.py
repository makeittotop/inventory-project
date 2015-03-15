from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from hr.models import Employee_Personal_Detail

# Register your models here.
class Employee_Personal_Detail_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields' : ['first_name', 'last_name', 'gender', 'country', 'dob', 'personal_email', 'personal_contact_number', \
        'passport_number', 'photo']}),
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
