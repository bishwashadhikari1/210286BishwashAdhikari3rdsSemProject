from django.test import Client, SimpleTestCase, TestCase
from django.urls import reverse, resolve 
from django.contrib.auth.models import User
from .views import register_page, login_page  , profile , edit_profile, delete_user
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

    def test_profile_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(profile) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,profile) # assertEquals compares function returned from resolve and the existing function
    
    def test_edit_profile_url(self):
        # test to see if "/" url exists or not for the home page (landing page)  
        url=reverse(edit_profile) # reverse helps to find url 
        # resolve helps to retrieve the function fo the url    
        self.assertEquals(resolve(url).func,edit_profile) # assertEquals compares function returned from resolve and the existing function
 

class TestViews(TestCase):

    def test_register(self):
        #create new user with username and password
        user = User.objects.create(username='test123')
        user.set_password('123123')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test123", password="123123")
        response = client.get(reverse(register_page))

        self.assertEquals(response.status_code, 200)
      
    def test_register_view(self):
        #create new user with username and password
        user = User.objects.create(username='test123')
        user.set_password('123123')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test123", password="123123")
        response = client.get(reverse(register_page))


        self.assertTemplateUsed(response, "user/register-form.html")    

    def test_updateProfile(self):

            client = Client()
    
            ewwser = User.objects.create(
                username= "kidq",
                password='123123',
                email="123@gmail.com",
                first_name='123123123123',
                last_name = '213141231324'
            )
            print(ewwser.username)
            response = client.post(reverse(edit_profile))
            self.assertEquals(response.status_code, 302)

    def test_delete(self):
        
        client = Client()
        ewwser = User.objects.create(
                username= "kidq",
                password='123123',
                email="123@gmail.com",
                first_name='123123123123',
                last_name = '213141231324'
            )
        print(ewwser.username)
        response = client.delete(reverse(delete_user))
        self.assertEquals(response.status_code, 302)