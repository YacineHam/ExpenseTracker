from django.forms import ModelForm
from .models import Receipt

class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = ['store_name', 'purchase_date', 'item_list', 'total_amount']