from django.db import models

# Create your models here.
class Asset_Computer(models.Model):
    CORES_CHOICES = (
        (8, 'Eight'),
        (16, 'Sixteen'),
        (32, 'Thirty Two'),
        (64, 'Sixty Four'),
        (96, 'Ninety Six'),
    )
    asset_cpu_cores = models.IntegerField('number of cpu cores', choices=CORES_CHOICES, default=32, max_length=200)

    GFX_CARD_CHOICES = (
      ('K4000', 'K4000'),
      ('K5000', 'K5000'),
      ('K3000', 'K3000'),
    )
    asset_gfx_card = models.CharField('types of gfx cards', choices=GFX_CARD_CHOICES, default='K4000', max_length=200)

    RAM_CHOICES = (
        (8, 'Eight'),
        (16, 'Sixteen'),
        (32, 'Thirty Two'),
        (64, 'Sixty Four'),
        (96, 'Ninety Six'),
    )
    asset_ram = models.IntegerField('amount of ram', choices=RAM_CHOICES, default=16, max_length=200)

    HARD_DISK_CHOICES = (
        ('250 GB', '250 GB'),
        ('500 GB', '500 GB'),
        ('1 TB', '1 TB'),
    )
    asset_hard_disk = models.CharField('types of hard disks', choices=HARD_DISK_CHOICES, default='500 GB', max_length=200)

    asset_external_nic = models.CharField('type of external nic', max_length=200)
                
class Asset_Detail(models.Model):
    CATEGORY_CHOICES=(
      ('work_station', 'Work Station'),
      ('server', 'Server'),
      ('render_farm', 'Render Farm'),
    )
    asset_category = models.CharField('category of asset', choices=CATEGORY_CHOICES, max_length=200)

    MANUFACTURER_CHOICES = (
      ('dell', 'DELL'),
      ('hp', 'HP'),
    )
    asset_manufacturer = models.CharField('manufacturer of asset', choices=MANUFACTURER_CHOICES, max_length=200)

    MODEL_CHOICES = (
      ('foo', 'bar'),
      ('toop', 'buzz' ),
    )
    asset_model = models.CharField('model of asset', choices=MODEL_CHOICES, max_length=200)

    asset_purchase_price = models.FloatField('purchase price of asset')

    asset_sell_price = models.FloatField('sell price of asset')

    asset_date_of_purchase = models.DateTimeField('date of purchase of asset')

    STATUS_CHOICES = (
      ('in_use', 'In Use'),
      ('spare', 'Spare'),
    )
    asset_status = models.CharField('status of asset', choices=STATUS_CHOICES, default='In Use', max_length=200)

    CONDITION_CHOICES = (
      ('new', 'New'),
      ('old', 'Old'),
      ('broken', 'Broken'),
    )
    asset_condition = models.CharField('condition of asset', choices=CONDITION_CHOICES, default='New', max_length=200)

    asset_checkout = models.CharField('checkout of asset', max_length=200)

    asset_notes = models.TextField('notes on asset')

    asset_name = models.CharField('name of asset', max_length=200)

    asset_computer = models.ForeignKey(Asset_Computer)
    
class Asset_Purchase_Detail(models.Model):
    asset_lpo = models.CharField('l.p.o of asset', max_length=200)
    asset_invoice = models.CharField('invoice of asset', max_length=200)
    asset_supplier = models.CharField('supplier of asset', max_length=200)

    asset_computer = models.ForeignKey(Asset_Computer)
    
