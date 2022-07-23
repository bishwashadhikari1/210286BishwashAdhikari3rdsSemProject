from django.urls import path
from . import views

urlpatterns = [ 
    path('subscription/', views.subs , name='subscription' ), 
    path('upgrade/<str:plan>/', views.upgrade_plan, name='upgradeplan'),
] 