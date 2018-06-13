from django import forms
from .models import Order
from localflavor.us.forms import USZipCodeField, USStateSelect
from localflavor.mx.forms import MXStateSelect, MXZipCodeField
from django_countries.fields import CountryField


class OrderCreateForm(forms.ModelForm):

    country = CountryField().formfield()
    #state = forms.CharField(widget=USStateSelect())
    postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address','postal_code','country', 'city', 'state']
