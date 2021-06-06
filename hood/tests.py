from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.

class NeighbourhoodTest(TestCase):
    def tearDown(self):
        Neighbourhood.objects.all().delete()
        Profile.objects.all().delete()
        Business.objects.all().delete()
        Post.objects.all().delete()

    def setUp(self):
        self.user = User.objects.create_user('john', email=None, password='secretpassword')
        self.hood = Neighbourhood(hood_name='Orleans', hood_location='Nairobi', occupants=3, admin=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighbourhood))