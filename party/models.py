from django.db import models

class party(models.Model):
    Select_city=models.CharField(max_length=50)
    Address=models.CharField(max_length=200)
    Mobile_no=models.IntegerField(default=True)
    GSTNO=models.CharField(max_length=50)
    Party_Type=models.CharField(max_length=50)
    Address_full=models.CharField(max_length=200)
    Email=models.EmailField(default="")
    Landline_no=models.IntegerField(default=True)
