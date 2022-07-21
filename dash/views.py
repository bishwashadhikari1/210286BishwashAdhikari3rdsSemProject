from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.core import session
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# @login_required(login_url='/login')
# def index(request):
#     # session(request.user.first_name,request.user.last_name)
#     event_triger()
#     return render(request, 'testgraph.html', context={'text':'5'})
    

def event_triger():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'event_sharif',
        {
            'type': 'send_message_to_frontend',
            'message': "event_trigered_from_views"
        }
    )
    

def msgfromoutside(request, username):
    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)('apiinfo',{
    #     'type':'apiInformation',
    #     'key':request.user.first_name,
    #     'secret': request.user.last_name
    # }   
    # )
    print('message sent')
    return render(request, 'testgraph.html', context={'text':'5','username':username})

