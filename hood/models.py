from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50)
    occupants = models.PositiveIntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, is_staff=True)

    def __str__(self):
        return self.hood_name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def create_neighbourhood(cls, hood_name: str, hood_location: str, occupants: int, admin: User):
        hood = Neighbourhood(hood_name=hood_name, hood_location=hood_location, occupants=occupants, admin=admin)
        hood.save_hood()

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        hood = cls.objects.get(id=neigborhood_id)
        return hood



class User(models.Model):
    image = CloudinaryField('image', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()
    bio = models.CharField(max_length=200)


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business_neighbourhood_id')
    email = models.EmailField()