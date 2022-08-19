from django import forms    
from django.forms import ModelForm
from .models import Sold, Products

class DateInput(forms.DateInput):
    input_type = 'date'


class SalesForm(ModelForm):
    class Meta:
        model = Sold
        fields = ['date', 'product_name', 'quantity_sold', 'unit_price', 'total',
                    'note']
        widgets = {'date': DateInput(),}

class ProductsForm(ModelForm):
    class Meta:
        model = Products 
        fields = ['product_name', 'quantity', 'expiry_date']
        widgets = {'expiry_date': DateInput(),}
