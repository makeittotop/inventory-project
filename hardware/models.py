from django.db import models

# Create your models here.
class Computer(models.Model):
    CORES_CHOICES = (
        (4, '4'),
        (6, '6'),
        (8, '8'),
        (16, '16'),
        (20, '20'),
    )
    asset_cpu_cores = models.IntegerField('CPU Cores', choices=CORES_CHOICES, max_length=200, blank=False)

    GFX_CARD_CHOICES = (
      ('Quadro-K4000', 'Quadro K4000'),
      ('Quadro-K5000', 'Quadro K5000'),
    )
    asset_gfx_card = models.CharField('Graphic Card', choices=GFX_CARD_CHOICES, max_length=200, blank=False)

    RAM_CHOICES = (
        (4, '4'),
        (16, '16'),
        (32, '32'),
        (64, '64'),
    )
    asset_ram = models.IntegerField('RAM', choices=RAM_CHOICES, max_length=200, blank=False)

    HARD_DISK_CHOICES = (
        ('250 GB', '250 GB'),
        ('500 GB', '500 GB'),
        ('1 TB', '1 TB'),
    )
    asset_hard_disk = models.CharField('H.D.D', choices=HARD_DISK_CHOICES, max_length=200, blank=False)

    EXTERNAL_NIC_CHOICES = (
      ('10G', '10G'),
    )
    asset_external_nic = models.CharField('External NIC', choices=EXTERNAL_NIC_CHOICES, max_length=200, blank=False)

    asset_serial_number = models.CharField('Serial Number', max_length=200, null=False, blank=False)

    asset_name = models.CharField('Name', max_length=200, null=False, blank=False)

    #asset_detail = models.OneToOneField(Asset_Detail, primary_key=True)
    #Purchase_Detail = models.OneToOneField(Purchase_Detail, primary_key=True)

    def __str__(self):
        return "{0} / {1}".format(self.asset_name, self.asset_serial_number)

class Asset_Detail(models.Model):
    CATEGORY_CHOICES=(
      ('work_station', 'Work Station'),
      ('server', 'Server'),
      ('render_farm', 'Render Farm'),
    )
    asset_category = models.CharField('Category', choices=CATEGORY_CHOICES, max_length=200, blank=False)

    MANUFACTURER_CHOICES = (
      ('dell', 'DELL'),
      ('hp', 'HP'),
    )
    asset_manufacturer = models.CharField('Manufacturer', choices=MANUFACTURER_CHOICES, max_length=200, blank=False)

    MODEL_CHOICES = (
      ('T360', 'T360'),
      ('Z420', 'Z420'),
      ('Z820', 'Z820'),
      ('9010', '9010' ),
    )
    asset_model = models.CharField('Model', choices=MODEL_CHOICES, max_length=200, blank=False)

    asset_purchase_price = models.FloatField('Purchase Price', null=True, blank=True)

    asset_sale_price = models.FloatField('Sale Price', null=True, blank=True)

    asset_date_of_purchase = models.DateTimeField('Purchase Date', null=True, blank=True)

    STATUS_CHOICES = (
      ('in_use', 'In Use'),
      ('spare', 'Spare'),
    )
    asset_status = models.CharField('Current Status', choices=STATUS_CHOICES, max_length=200, blank=False)

    CONDITION_CHOICES = (
      ('new', 'New'),
      ('old', 'Old'),
      ('broken', 'Broken'),
      ('in-repair', 'In Repair'),
    )
    asset_condition = models.CharField('Condition', choices=CONDITION_CHOICES, max_length=200, blank=False) 

    asset_checkout = models.CharField('Assignee', max_length=200, null=True, blank=True)

    asset_notes = models.TextField('Notes', null=True, blank=True)

    #asset_name = models.CharField('Identifier/Name', max_length=200, blank=False)

    #computer = models.ForeignKey(Computer)
    computer = models.OneToOneField(Computer, null=False, blank=False)

    def __str__(self):
        return "Asset Details"
    
class Purchase_Detail(models.Model):
    asset_lpo = models.CharField('P.O. Number', max_length=200, null=False, blank=False)
    asset_invoice = models.CharField('Invoice Number', max_length=200, null=False, blank=False)
    asset_supplier = models.CharField('Supplier Name', max_length=200, null=False, blank=False)

    #computer = models.ForeignKey(Computer)
    computer = models.OneToOneField(Computer)
    
    def __str__(self):
        return "Purchase Details"
    
