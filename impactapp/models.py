from django.db import models

# Create your models here.
class contact(models.Model):
    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Company=models.CharField(max_length=200)
    Contact=models.BigIntegerField()
    Reason=models.CharField(max_length=250)
    Message=models.TextField()

    class Meta:
        db_table='contact'
        
class product(models.Model):
    Name=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='media',default='')
    Description=models.TextField()
    CompanyName=models.CharField(max_length=200)
    Price=models.BigIntegerField()

    class Meta:
        db_table='product'
