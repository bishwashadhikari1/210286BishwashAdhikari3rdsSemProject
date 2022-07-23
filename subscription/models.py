from django.db import models
from django.contrib.auth.models import User
from datetime import date
class Subscription(models.Model): 
    sub_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    current_plan = models.TextField(default='basic')
    expiration = models.DateField(null=True)
    class Meta:
         db_table='subscription'
    def __str__(self) :
        return self.owner

    def isExpired(self):
        return self.expiration < date

class TransactionHistory(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    current_subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    plan = models.TextField()
    created = models.DateTimeField()
    expiry = models.DateTimeField()
    currency = models.TextField()
    network = models.TextField()
    timePeriod = models.TextField()
    transactionId = models.TextField()
    verified = models.BooleanField()

    def __str__(self):
        return self.transaction_id