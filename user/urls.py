from django.urls import path
from user import views
urlpatterns = [
    path("/login-form", views.login_page),
    # path("/login"),
    path("register-form", views.register_page),
    # path("/register"),
]