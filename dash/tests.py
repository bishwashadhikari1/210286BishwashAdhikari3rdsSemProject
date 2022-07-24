from django.test import SimpleTestCase, TestCase
from django.test import Client
from django.urls import reverse, resolve 
from .views import dashboard, static_dash
from django.contrib.auth.models import User
class TestUrls(SimpleTestCase):

    def test_dashboard_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(dashboard, args=[1]) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,dashboard) # assertEquals compares function returned from resolve and the existing function

    def test_staticdashboard_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(static_dash, args=[1]) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,static_dash) # assertEquals compares function returned from resolve and the existing function

class TestViews(TestCase):
    def test_statuc_daaaaaa(self):

        client = Client()
        ewwser = User.objects.create(
                username= "kidqp",
                password='123123',
                email="123@gmail.com",
                first_name='sD6Er0DWH3eVIt1AejxuFiZVDFtVhtrCeXdmjrer3pl8pu2iy6Etm8S8QhSQImUN',
                last_name = 'pgcZsyVi4V7pC1MWaMNloqWSEDqhuEHLZ46Y6h8rHezzpwfiKyAn2v7yQ5QMxbSt'
            )
        
        
        response = client.get(reverse(static_dash,args=[1]))
        self.assertEquals(response.status_code, 302)
    
    def test_dashboard(self):

        client = Client()
        
        
        
        response = client.get(reverse(dashboard,args=[1]))
        self.assertEquals(response.status_code, 302)
        
