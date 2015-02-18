from django.contrib import admin
from physical_assets.models import Asset_Computer, Asset_Detail, Asset_Purchase_Detail

# Register your models here.

class Asset_Detail_Inline(admin.StackedInline):
    model = Asset_Detail

class Asset_Purchase_Detail_Inline(admin.StackedInline):
    model = Asset_Purchase_Detail

class Asset_Computer_Admin(admin.ModelAdmin):
    inlines = [Asset_Detail_Inline, Asset_Purchase_Detail_Inline]

admin.site.register(Asset_Computer, Asset_Computer_Admin)
