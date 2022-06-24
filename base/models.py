# from django.db import models

# class Users(models.Model):
#     username = models.CharField(max_length=50, primary_key=True)
#     password = models.CharField(max_length=32, null=False, default=False)
#     email = models.CharField(max_length=50, null=False, default=False )
#     apikey = models.CharField(max_length=100, default="", null=False )
#     apisecret = models.CharField(max_length=100, default="", null=False) 
 

#     class Meta:
#         db_table = 'users'

# from pyexpat import model
# from tkinter import CASCADE
# from django.db import models
# from django.forms import IntegerField, PasswordInput

# # Create your models here.

# class Users(models.Model):
#     username = models.TextField(max_length=50, null=False, primary_key=True)
#     password = models.CharField(max_length=32, null=False)
#     email = models.EmailField(max_length=50, null=True)
#     api_key = models.TextField(max_length=100, unique=True)
#     api_secret = models.TextField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username

#     def edit(request,username):
#         print(id)
#         data=Users.get(username=username)    

# class Prefrences(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     risk = models.FloatField()
#     positionSize = models.IntegerField()
#     tickerQuantity=models.IntegerField()
#     strategy=models.TextField()
#     timeFrame = models.IntegerField()
#     riskReward = models.FloatField()

#     def __str__(self):
#         return self.user


# class Plan(models.Model):
#     owner = models.ForeignKey(Users, on_delete=models.CASCADE)
#     current_plan = models.TextField(default='BASIC')
#     expiration = models.DateField(null=True)
#     def __str__(self):
#         return self.owner

# class transactionHistory(models.Model):
#     transaction_id = models.TextField(primary_key=True)
#     # subscription = models.ForeignKey(Plan, on_delete=models.CASCADE)
#     created = models.DateTimeField()
#     expiry = models.DateTimeField()
#     currency = models.TextField()
#     network = models.TextField()
#     timePeriod = models.TextField()
#     transactionId = models.TextField()
#     verified = models.BooleanField()

#     def __str__(self):
#         return self.transaction_id

         