from django.db import models
 

from base.models import Users
class Preferances(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, auto_created=True)
    risk = models.FloatField()
    positionsize = models.IntegerField()
    noticker=models.IntegerField()
    strategy=models.CharField(max_length=5)
    timeframe = models.IntegerField()
    rrratio = models.FloatField()

    class Meta:
         db_table='preferances'
    def __str__(self) :
        return self.id
