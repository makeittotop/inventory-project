from django.db import models

# Create your models here.
class Asset_Computer(models.Model):
    CORES_CHOICES = (
        (8, '8'),
        (16, '16'),
        (32, '32'),
        (64, '64'),
        (96, '96'),
    )
    asset_cpu_cores = models.IntegerField('CPU Cores', choices=CORES_CHOICES, default=32, max_length=200)

    GFX_CARD_CHOICES = (
      ('K4000', 'K4000'),
      ('K5000', 'K5000'),
      ('K3000', 'K3000'),
    )
    asset_gfx_card = models.CharField('Graphic Card', choices=GFX_CARD_CHOICES, default='K4000', max_length=200)

    RAM_CHOICES = (
        (8, '8'),
        (16, '16'),
        (32, '32'),
        (64, '64'),
        (96, '96'),
    )
    asset_ram = models.IntegerField('RAM', choices=RAM_CHOICES, default=16, max_length=200)

    HARD_DISK_CHOICES = (
        ('250 GB', '250 GB'),
        ('500 GB', '500 GB'),
        ('1 TB', '1 TB'),
    )
    asset_hard_disk = models.CharField('H.D.D', choices=HARD_DISK_CHOICES, default='500 GB', max_length=200)

    asset_external_nic = models.CharField('External NIC', max_length=200)
                
class Asset_Detail(models.Model):
    CATEGORY_CHOICES=(
      ('work_station', 'Work Station'),
      ('server', 'Server'),
      ('render_farm', 'Render Farm'),
    )
    asset_category = models.CharField('Category', choices=CATEGORY_CHOICES, max_length=200)

    MANUFACTURER_CHOICES = (
      ('dell', 'DELL'),
      ('hp', 'HP'),
    )
    asset_manufacturer = models.CharField('Manufacturer', choices=MANUFACTURER_CHOICES, max_length=200)

    MODEL_CHOICES = (
      ('foo', 'bar'),
      ('toop', 'buzz' ),
    )
    asset_model = models.CharField('Model', choices=MODEL_CHOICES, max_length=200)

    asset_purchase_price = models.FloatField('Purchase Price', default=None)

    asset_sale_price = models.FloatField('Sale Price', default=None)

    asset_date_of_purchase = models.DateTimeField('Purchase Date')

    STATUS_CHOICES = (
      ('in_use', 'In Use'),
      ('spare', 'Spare'),
    )
    asset_status = models.CharField('Current Status', choices=STATUS_CHOICES, default='In Use', max_length=200)

    CONDITION_CHOICES = (
      ('new', 'New'),
      ('old', 'Old'),
      ('broken', 'Broken'),
    )
    asset_condition = models.CharField('Condition', choices=CONDITION_CHOICES, default='New', max_length=200)

    asset_checkout = models.CharField('In use by', max_length=200)

    asset_notes = models.TextField('Notes')

    asset_name = models.CharField('Identifier/Name', max_length=200)

    asset_computer = models.ForeignKey(Asset_Computer)
    
class Asset_Purchase_Detail(models.Model):
    asset_lpo = models.CharField('P.O.', max_length=200)
    asset_invoice = models.CharField('Invoice', max_length=200)
    asset_supplier = models.CharField('Supplier', max_length=200)

    asset_computer = models.ForeignKey(Asset_Computer)
    
