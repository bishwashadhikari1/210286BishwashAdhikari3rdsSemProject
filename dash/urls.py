from django.urls import path

from .views import dashboard, static_dash
urlpatterns = [
    path('graph/<str:username>/', dashboard),
    path('dashboard/<str:username>', static_dash)
    ]