from django.test import TestCase
from .models import (Image,Location,Category)

# Create your tests here.
class ImageTestCase(TestCase):
    # set up
    def setUp(self):
        self.images = Image(name='test',description='its a awesome image',image='url',updateAt='28/02/2022' )



    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.images,Image))