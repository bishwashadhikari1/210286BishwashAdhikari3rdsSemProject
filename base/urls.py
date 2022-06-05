from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('users/<str:pk>/',views.users, name='users'),

]
