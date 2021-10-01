from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm , forms
from .models import *

class AddProductForm(forms.ModelForm):

    category_name = forms.CharField(max_length=30, required=False)
    description = forms.CharField(max_length=100, required=False)
    buying_price= forms.IntegerField( required=False)
    selling_price = forms.IntegerField( required=False)
    purchase = forms.IntegerField( required=False)
    sale= forms.IntegerField( required=False)
    class Meta:
        model=Product
        fields=[
            'product_name',
            'category_name',
            'description',
            'buying_price',
            'selling_price',
            'purchase',
            'sale',
            'stock',

        ]

