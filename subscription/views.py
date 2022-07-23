from locale import currency
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from traitlets import Int, Integer
from subscription.forms import TransactionForm
from subscription.models import Subscription, TransactionHistory
from datetime import date
from dateutil.relativedelta import relativedelta




@login_required
def subs(request):
    sub = Subscription.objects.get(owner = request.user)
    print(sub.current_plan)
    return render(request, 'subscription.html', {'sub': sub})


@login_required
def upgrade_plan(request, plan):
    if request.method == "POST":
        
        expiry  = date.today() + relativedelta(months=+int(request.POST['time']))
        sub = Subscription.objects.get(owner = request.user)
        formm = TransactionHistory(
            current_subscription = sub,
            created= date.today(),
            expiry=expiry,
            currency=request.POST['currency'],
            network=request.POST['network'],
            transactionId= request.POST['txnid'],
            timePeriod= request.POST['time'],
            plan=plan,
            verified= False
        )
        formm.save()
        sub.current_plan = plan
        sub.expiration = expiry
        sub.save()
        return redirect('/subscription')
    return render(request, 'subscriptioncheckout.html', {'plan':plan})