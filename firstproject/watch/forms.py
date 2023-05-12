from django import forms
class Storedata(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    payment = forms.CharField()
    