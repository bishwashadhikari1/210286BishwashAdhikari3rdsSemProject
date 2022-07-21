from django.urls import path
from .views import msgfromoutside
urlpatterns = [
    path('graph/<str:username>/', msgfromoutside),
    ]