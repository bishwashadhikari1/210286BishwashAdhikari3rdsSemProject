from django.urls import path
from user import views
urlpatterns = [
    path("login/", views.login_page),
    path('deleteuser/', views.delete_user),
    path("signup/", views.register_page),
    path("profile/edit/" , views.edit_profile),
    path("profile/", views.profile)
]