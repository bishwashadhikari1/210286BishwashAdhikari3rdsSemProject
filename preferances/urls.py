
from django.urls import path
from . import views
urlpatterns = [
    path('preferances/', views.preferances, name='preferances'),
    path('preferancesmodified/', views.preferancesmodified, name='preferancesmodified' ),
]
