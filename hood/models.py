from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=50)
    hood_location = models.CharField(max_length=50)
    occupants = models.PositiveIntegerField(default=0)
    admin = models.ForeignKey(User(is_staff=True), on_delete=models.CASCADE)

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

    @classmethod
    def update_neighborhood(cls, neigborhood_id, new_hood_name: str):
        hood = cls.objects.filter(id=neigborhood_id).update(hood_name=new_hood_name)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    image = CloudinaryField('image', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    bio = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business_neighbourhood_id')
    email = models.EmailField()

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.get(id=business_id)
        return business

    @classmethod
    def update_business(cls, business_id, new_business_name):
        business = cls.objects.filter(id=business_id).update(business_name=new_business_name)


class Post(models.Model):
    title = models.CharField(max_length=50)
    context = models.CharField(max_length=1500)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.title