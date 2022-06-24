from django.db import models
from base.models import Users

class Subscription(models.Model): 
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    current_plan = models.TextField(default='BASIC')
    expiration = models.DateField(null=True)
    class Meta:
         db_table='subscription'
    def __str__(self) :
        return self.owner

class transactionHistory(models.Model):
    transaction_id = models.TextField(primary_key=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    created = models.DateTimeField()
    expiry = models.DateTimeField()
    currency = models.TextField()
    network = models.TextField()
    timePeriod = models.TextField()
    transactionId = models.TextField()
    verified = models.BooleanField()

    def __str__(self):
        return self.transaction_id