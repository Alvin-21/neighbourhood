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

    def test_save_method(self):
        self.hood.save_hood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_method(self):
        self.hood.save_hood()
        self.hood.delete_hood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood) == 0)

    def test_create_neighbourhood(self):
        hood = Neighbourhood.create_neighbourhood('Bywater', 'Nairobi', 8, self.user)
        hood_len = Neighbourhood.objects.all()
        self.assertTrue(len(hood_len) > 0)

    def test_find_neigborhood(self):
        self.hood.save_hood()
        hood = Neighbourhood.find_neigborhood(self.hood.id)
        self.assertTrue(hood, self.hood)

    def test_update_neighborhood(self):
        self.hood.save_hood()
        self.hood.update_neighborhood(self.hood.id, 'Midcity')
        hood_name = Neighbourhood.objects.filter(hood_name='Midcity')
        self.assertTrue(len(hood_name) == 1)