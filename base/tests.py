from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve 
from .views import home
class TestUrls(SimpleTestCase):

    def test_home_url(self):
        # test to see if "/" url exists or not for the home page (landing page)
        url=reverse(home) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url
        self.assertEquals(resolve(url).func,home) # assertEquals compares function returned from resolve and the existing function