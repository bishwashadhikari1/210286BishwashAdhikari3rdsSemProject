from django.test import SimpleTestCase, TestCase
from django.test import Client
from django.urls import reverse, resolve 
from .views import logout_fn 
from django.contrib.auth.models import User
class TestUrls(SimpleTestCase):

    def test_logout_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(logout_fn) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,logout_fn) # assertEquals compares function returned from resolve and the existing function
