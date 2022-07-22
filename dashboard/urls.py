from django.urls import path
from . import views

urlpatterns =  [ 
#  path('dashboard/', views.dashboard, name='dashboard'),
 path ('logout/', views.logout_fn, name='logout'),
#  path('rebase/', views.dbrebase, name='dbrebase'),
#  path('refresh/', views.refresh, name='refresh'),
]