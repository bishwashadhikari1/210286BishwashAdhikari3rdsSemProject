
from django.shortcuts import  render
from preferances.forms import PreferancesForm
from django.contrib.auth.decorators import login_required
from preferances.models import Preferances
from subscription.models import Subscription

@login_required(login_url='/user/login')
def preferances(request):
    sub = Subscription.objects.get(owner = request.user)
    plan = sub.current_plan
    pref = Preferances.objects.get(user_id = request.user.id)
    if request.method=="POST":  
        formm = PreferancesForm({
            'user' : request.user,
            'risk' : request.POST['risk'],
            'noticker':request.POST['noticker'],
            'strategy':request.POST['strategy'],
            'timeframe':request.POST['timeframe'],
            'rrratio': request.POST['rrratio'],
            'positionsize': request.POST['positionsize'],
        }, instance=pref
        )
        print(pref.positionsize)
        if formm.is_valid():  
            formm.save()
            return render(request, 'preferancesmodified.html')   
        else:
            print(formm.errors.as_data)
    return render(request, 'preferances.html', {'preferances': pref, 'plan':plan})   

