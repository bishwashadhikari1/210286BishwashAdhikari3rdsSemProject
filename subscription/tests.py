from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from requests import request
from subscription.models import Subscription 
from .views import subs, upgrade_plan
class TestUrls(SimpleTestCase):

    def test_subscription_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(subs) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,subs) # assertEquals compares function returned from resolve and the existing function
    

class TestViews(TestCase):   
    def update_subcription(self):
            client = Client()
            logged_in = client.login(username="test1233", password="test123")
            ewwser = User.objects.create(
                username= "kidq",
                password='123123',
                email="123@gmail.com",
                first_name='123123123123',
                last_name = '213141231324'
            )
            c_order = Subscription.objects.create(
                owner = ewwser
            )

            response = client.get(reverse(upgrade_plan,args =[1]))
            self.assertEquals(response.status_code, 302)
    
    def test_subs(self):
       
        client = Client()
        ewwser = User.objects.create(
                username= "kidqp",
                password='123123',
                email="123@gmail.com",
                first_name='123123123123',
                last_name = '213141231324'
            )
        
        c_order = Subscription.objects.create(
            sub_id = 1,
            owner = ewwser,
            current_plan = "asd",
        )
        
        response = client.get(reverse(subs))
        self.assertEquals(response.status_code, 302)

    
    
        


        
    
