from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=32, null=False, default=False)
    email = models.CharField(max_length=50, null=False, default=False )
    apikey = models.CharField(max_length=100, default="", null=False )
    apisecret = models.CharField(max_length=100, default="", null=False) 
 

    class Meta:
        db_table = 'users'

