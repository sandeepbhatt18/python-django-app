from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class survey(models.Model):
    name = models.CharField(max_length=65)
    address = models.CharField(max_length=256)
    # address = models.TextField(blank=True)
    contact_No = models.CharField(max_length=65,unique=True,default='')
    email = models.EmailField(max_length=65,unique=True,blank=True)

class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # # pip install pillow to use this!
    # # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    # profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
