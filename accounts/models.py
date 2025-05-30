from django.db import models
from django.contrib.auth.models import User

class HotelUser(User):
      phone_number = models.CharField(max_length=15,unique=True)
      profile_photo = models.ImageField(upload_to='profile')
      email_otp = models.CharField(max_length=100, null=True,blank=True)
      otp = models.CharField(max_length=10, null=True, blank=True)

class HotelVendor(User):
      phone_number = models.CharField(max_length=15,unique=True)
      profile_photo = models.ImageField(upload_to='profile')
      email_otp = models.CharField(max_length=100, null=True,blank=True)
      otp = models.CharField(max_length=10, null=True, blank=True)
      
class Ammenites(models.Model):
      name=models.CharField(max_length=100)
      icon=models.ImageField(upload_to='hotels')
      
class Hotel(models.Model):
      hotel_name=models.CharField(max_length=100)
      hotel_location=models.TextField()
      hotel_price=models.FloatField()
      hotel_offer_price=models.FloatField()
      hotel_description = models.TextField()
      hotel_ammenties= models.ManyToManyField(Ammenites)
      hotel_owner=models.ForeignKey(HotelVendor,on_delete=models.CASCADE,  related_name="hotels" )
      is_active=models.BooleanField(default=True)
      
class HotelImages(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,  related_name="hotel_images" )
    images= models.ImageField(upload_to='hotels')
    
class HotelManager(models.Model):
      hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,  related_name="hotel_manager" )
      manager_name=models.CharField(max_length=100)
      manager_contact=models.CharField(max_length=100)