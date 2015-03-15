from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Employee_Personal_Detail(models.Model):
    first_name = models.CharField('First Name', max_length=200, blank=False)
    last_name = models.CharField('Last Name', max_length=200, blank=False)
    gender_choices = (
        (1, 'Male'),
        (2, 'Female'),
    )
    gender = models.SmallIntegerField('Gender', choices=gender_choices, blank=False)
    country = models.CharField('Home Country', max_length=200, null=True, blank=True)
    dob = models.DateField('Date of Birth', blank=True)
    personal_email = models.EmailField('Personal Email', max_length=200, blank=False)
    personal_contact_number = models.CharField('Contact Number', max_length=200, blank=False)
    passport_number = models.CharField('Passport Number', max_length=200, blank=False)
    photo = models.ImageField('Employee Photo', upload_to='photos', null=True, blank=True)

    code = models.CharField('Employee Code', max_length=200, blank=False)
    hire_date = models.DateField('Hire Date', blank=False)
    end_hire_date = models.DateField('End Hire Date', null=True, blank=True)
    department_choices = (
        ('animation', 'Animation'),
        ('rigging', 'Rigging'),
        ('lighting', 'Lighting'),
        ('compositing', 'Compositing'),
        ('pipeline', 'Pipeline'),
        ('information_technology', 'I.T.'),
        ('human_resources', 'H.R.'),
    )
    department = models.CharField('Department',choices=department_choices, max_length=200, blank=False)
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField('Status', choices=status_choices, max_length=200, blank=False)
    official_email = models.EmailField('Official Email', max_length=200, null=True, blank=False)
    designation = models.CharField('Designation', max_length=200, null=False, blank=False)
    notes = models.TextField("Notes", null=True, blank=True)

    def thumb(self):
        if self.photo:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % (self.photo.url))
        else:
            return mark_safe(u'<img src="%s" width=60 height=60 />' % ('/media/photos/placeholder.png'))
    thumb.short_description = 'Photo Preview'
    thumb.allow_tags = True

    def __str__(self):
        return "{0} {1}".format(self.first_name.capitalize(), self.last_name.capitalize())
