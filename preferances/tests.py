from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth import  authenticate
from .views import preferances
from django.contrib.auth.models import User
from .models import Preferances
class TestUrls(SimpleTestCase):

    def test_preferances_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(preferances) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,preferances) # assertEquals compares function returned from resolve and the existing function

