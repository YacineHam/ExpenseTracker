from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Receipt
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import ReceiptForm
from django.views.generic.edit import DeleteView

# Create your views here.



class ReceiptListView(ListView):
    model = Receipt
    template_name = 'receipts/list.html'

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)


class ReceiptDetailView(DetailView):
    model = Receipt
    template_name = 'receipts/detail.html'


class ReceiptCreateView(CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipts/form.html'

class ReceiptUpdateView(UpdateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipts/form.html'

class ReceiptDeleteView(DeleteView):
    model = Receipt
    template_name = 'receipts/delete.html'
    success_url = '/'