from django.db import models
from django.utils.html import mark_safe

import sys

# Create your models here.

class Employee(models.Model):
    employee_first_name = models.CharField('First Name', max_length=200, blank=False)
    employee_last_name = models.CharField('Last Name', max_length=200, blank=False)
    gender_choices = (
        (1, 'Male'),
        (2, 'Female'),
    )
    employee_gender = models.SmallIntegerField('Gender', choices=gender_choices, blank=False)
    employee_country = models.CharField('Home Country', max_length=200, null=True, blank=True)
    employee_dob = models.DateField('Date of Birth', blank=True)
    employee_personal_email = models.EmailField('Personal Email', max_length=200, blank=False)
    employee_personal_contact_number = models.CharField('Contact Number', max_length=200, blank=False)
    employee_passport_number = models.CharField('Passport Number', max_length=200, blank=False)
    employee_photo = models.ImageField('Employee Photo', upload_to='photos', null=True, blank=True)

    employee_code = models.CharField('Employee Code', max_length=200, blank=False)
    employee_hire_date = models.DateField('Hire Date', blank=False)
    employee_end_hire_date = models.DateField('End Hire Date', null=True, blank=True)
    department_choices = (
        ('animation', 'Animation'),
        ('rigging', 'Rigging'),
        ('lighting', 'Lighting'),
        ('compositing', 'Compositing'),
        ('pipeline', 'Pipeline'),
        ('information_technology', 'I.T.'),
        ('human_resources', 'H.R.'),
    )
    employee_department = models.CharField('Department',choices=department_choices, max_length=200, blank=False)
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    employee_status = models.CharField('Status', choices=status_choices, max_length=200, blank=False)
    employee_official_email = models.EmailField('Official Email', max_length=200, null=True, blank=False)
    employee_notes = models.TextField("Notes", null=True, blank=True)

    def thumb(self):
        if self.employee_photo:
            print >>sys.stderr, self.employee_photo.url

            return mark_safe(u'<img src="%s" width=60 height=60 />' % (self.employee_photo.url))
        else:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % ('/media/photos/placeholder.png'))
    thumb.short_description = 'Photo'
    thumb.allow_tags = True

    def __str__(self):
        return "{0} {1}".format(self.employee_first_name.capitalize(), self.employee_last_name.capitalize())
