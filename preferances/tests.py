from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve 
from .views import preferances , preferancesmodified
class TestUrls(SimpleTestCase):

    def test_preferances_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(preferances) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,preferances) # assertEquals compares function returned from resolve and the existing function

    # def test_preferancesmodified_url(self):
    #     # test to see if "/" url exists or not for the home page (landing page)  
    #     url=reverse(preferancesmodified) # reverse helps to find url 
    #     # resolve helps to retrieve the function fo the url    
    #     self.assertEquals(resolve(url).func,preferancesmodified) # assertEquals compares function returned from resolve and the existing function

