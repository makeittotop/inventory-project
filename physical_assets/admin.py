from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from physical_assets.models import Asset_Computer, Asset_Detail, Asset_Purchase_Detail

# Register your models here.

class Asset_Detail_Inline(admin.StackedInline):
    model = Asset_Detail
    extra = 1

class Asset_Purchase_Detail_Inline(admin.StackedInline):
    fieldsets = [
        ('Purchase Details', {'fields': ['asset_lpo', 'asset_invoice', 'asset_supplier']}),
    ]
    model = Asset_Purchase_Detail
    extra = 1

class Asset_Computer_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Specification', {'fields': ['asset_cpu_cores', 'asset_gfx_card', 'asset_ram', 'asset_hard_disk', 'asset_external_nic']}),
    ]
    inlines = [Asset_Detail_Inline, Asset_Purchase_Detail_Inline]

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Asset_Computer, Asset_Computer_Admin)
