from django import forms
from base.models import User
class RegisterForm(forms.Form):
    class Meta:
        model = User
        field = "__all__"