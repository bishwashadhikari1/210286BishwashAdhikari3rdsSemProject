from django.contrib import admin
from subscription.models import Subscription, TransactionHistory
from preferances.models import Preferances
# Register your models here.

admin.site.register(Subscription)
admin.site.register(TransactionHistory)
admin.site.register(Preferances)


