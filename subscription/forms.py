
from django import forms
from subscription.models import TransactionHistory
class TransactionForm(forms.ModelForm):
    # class Meta:
    #     model = TransactionHistory
    #     fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(TransactionForm,self).__init__(*args,**kwargs)