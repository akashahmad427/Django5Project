from django import forms
from .models import Sellinfo
class Selling(forms.ModelForm):
    class Meta:
        model = Sellinfo
        fields = ['first_name','last_name','father_name','cnic','address','city','email','phone']
        