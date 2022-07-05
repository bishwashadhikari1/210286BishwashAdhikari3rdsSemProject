from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve 
from .views import register_page, login_page  
class TestUrls(SimpleTestCase):

    def test_signup_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(register_page) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,register_page) # assertEquals compares function returned from resolve and the existing function

    def test_login_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(login_page) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,login_page) # assertEquals compares function returned from resolve and the existing function
 

