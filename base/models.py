from django.db import models

class User(models.Model):
    username = models.CharField(primary_key = True, max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    apikey = models.CharField(max_length=50)
    apisecret = models.CharField(max_length=50)

