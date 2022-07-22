from tkinter import CASCADE
from django.db import models 
from django.contrib.auth.models import User
class Preferances(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, auto_created=True )
    risk = models.FloatField(default=1.0)
    positionsize = models.IntegerField(default=10)
    noticker=models.IntegerField(default=1)
    strategy=models.CharField(max_length=15, default='rsi')
    timeframe = models.IntegerField(default=30)
    rrratio = models.FloatField(default=1.5)

    class Meta:
         db_table='preferances'
    def __str__(self) :
        return f'{self.id}'
 

