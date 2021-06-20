from django.db import models
from datetime import datetime
class Claim(models.Model):
    name = models.CharField(max_length=122,default="")
    email = models.CharField(max_length=122,default="")
    mob = models.CharField(max_length=122,default="")
    vehicle_year_make= models.DateField(default=datetime.today())
    vehicle_model = models.CharField(max_length=122,default="")
    vehicle_no = models.CharField(max_length=122,default="")
    accident_time = models.DateTimeField(default=datetime.today())
    location_of_loss = models.CharField(max_length=122,default="")
    type_of_loss = models.CharField(max_length=122,default="")
    description_of_loss = models.TextField(max_length=122,default="")
    policy_report_lodge = models.CharField(max_length=122,default="")
    any_body_injured = models.CharField(max_length=122,default="")
    loss_image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', null=True,blank=True)
    approve = models.IntegerField(default=0)

    def __str__(self):
        return self.name + self.vehicle_model
