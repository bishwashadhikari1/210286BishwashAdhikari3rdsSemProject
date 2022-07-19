from django.test import SimpleTestCase, TestCase
from django.test import Client
from django.urls import reverse, resolve 
from .views import dashboard, logout_fn
from django.contrib.auth.models import User
class TestUrls(SimpleTestCase):

    def test_dashboard_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(dashboard) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,dashboard) # assertEquals compares function returned from resolve and the existing function

    def test_logout_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(logout_fn) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,logout_fn) # assertEquals compares function returned from resolve and the existing function
class TestViews(TestCase):
    user = User(username='testuser')
    user.set_password('asdsad')
    user.save()
    def test_dashboard_view(self):
        loggedin = Client.login(username='testuser', password = "asdsad") 
        client = Client()
        response = Client.get(reverse('dashboard'))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/dashboard.html')