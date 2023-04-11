from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

def upload_to(instance, filename):
   return 'post/{filename}'.format(filename=filename)

class Employee(models.Model):
   profile_picture = models.ImageField(_("Image"), upload_to=upload_to, default='post/ibro.jpg')
   full_name = models.CharField(max_length=200)
   email = models.CharField(max_length=100)
   contact= models.CharField(max_length=20)
   address = models.TextField()

   def __str__(self):
    return self.full_name
