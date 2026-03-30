from django.db import models
# from django.contrib.auth.forms import UserCreationForm 

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    agency = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=250,null=True, blank=True)
    uploadfile = models.FileField(upload_to="property_img",max_length=250, null=True, default=None)
    upload_img = models.ImageField(upload_to="property_img/",max_length=250 , null=True, default=None) # height_field='20px', width_field='20px', 
    addre = models.CharField(max_length=250,null=True, blank=True)
    def __str__(self):
       return self.name
       

class Category_registration(models.Model):
    reg_no = models.CharField(max_length=200,null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    firm = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=250,null=True, blank=True)
    desic = models.CharField(max_length=250,null=True, blank=True)
    uploadfile = models.FileField(upload_to="property_img/",max_length=280, null=True, default=None)
    upload_img = models.ImageField(upload_to="property_img/",max_length=250 , null=True, default=None)
    addre = models.CharField(max_length=250,null=True, blank=True)
    def __str__(self):
       return self.name
    
class Contact_data (models.Model):
     name = models.CharField(max_length=200,null=True, blank=True)
     email = models.EmailField(max_length=100, null=True, blank=True)
     cnic = models.CharField(max_length=200, null=True, blank=True)
     phone = models.CharField(max_length=250,null=True, blank=True)
     comment = models.CharField(max_length=250,null=True, blank=True)
     def __str__(self):
       return self.name
    

