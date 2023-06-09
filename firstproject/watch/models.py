from django.db import models

# Create your models here.
class Sellinfo(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=80)
    father_name= models.CharField(max_length=90)
    cnic = models.IntegerField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=90,default='New York')
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()

class Photo(models.Model):
    img = models.ImageField(upload_to='myimage')