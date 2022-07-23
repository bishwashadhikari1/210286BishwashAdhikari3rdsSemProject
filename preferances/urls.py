
from django.urls import path
from . import views
urlpatterns = [
    path('preferances/', views.preferances, name='preferances'),
]
