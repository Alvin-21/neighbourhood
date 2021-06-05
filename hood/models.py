from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50)
    occupants = models.PositiveIntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, is_staff=True)


class User(models.Model):
    image = CloudinaryField('image', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()
    bio = models.CharField(max_length=200)