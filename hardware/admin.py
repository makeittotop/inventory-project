from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from hardware.models import Computer, Asset_Detail, Purchase_Detail

# Register your models here.

class Asset_Detail_Inline(admin.StackedInline):
    model = Asset_Detail
    #extra = 1

class Purchase_Detail_Inline(admin.StackedInline):
    model = Purchase_Detail
    #extra = 1

class Computer_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Specification', {'fields': ['asset_name', 'asset_serial_number', 'asset_cpu_cores', 'asset_gfx_card', 'asset_ram', 'asset_hard_disk', 'asset_external_nic']}),
    ]
    inlines = [Asset_Detail_Inline, Purchase_Detail_Inline]

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Computer, Computer_Admin)
