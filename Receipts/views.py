from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Receipt
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import ReceiptForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



class ReceiptListView(LoginRequiredMixin,ListView):
    model = Receipt
    template_name = 'receipts/list.html'

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)


class ReceiptDetailView(LoginRequiredMixin,DetailView):
    model = Receipt
    template_name = 'receipts/detail.html'


class ReceiptCreateView(LoginRequiredMixin,CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipts/form.html'
    success_url = reverse_lazy('receipt-list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user here
        return super().form_valid(form)

class ReceiptUpdateView(LoginRequiredMixin,UpdateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'receipts/form.html'
    success_url = reverse_lazy('receipt-list')


class ReceiptDeleteView(LoginRequiredMixin,DeleteView):
    model = Receipt
    template_name = 'receipts/delete.html'
    success_url = '/'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')     
    template_name = 'auth/signup.html'



