from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(default = 'profile_pics/default.jpeg', upload_to = 'profile_pics')
    date = models.DateField(default=timezone.now)
    address = models.CharField(max_length= 50, blank = True)
    city_town = models.CharField(max_length= 50, blank = True)
    country = models.CharField( max_length= 50, blank = True )
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
# Create your models here.
