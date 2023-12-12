"""
URL configuration for ExpenseTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from receipts.views import ReceiptListView,ReceiptDetailView,ReceiptCreateView,ReceiptUpdateView,ReceiptDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReceiptListView.as_view(), name='receipt-list'),
    path('receipt/<int:pk>/', ReceiptDetailView.as_view(), name='receipt-detail'),
    path('receipt/new/', ReceiptCreateView.as_view(), name='receipt-create'),
    path('receipt/<int:pk>/edit/', ReceiptUpdateView.as_view(), name='receipt-update'),
    path('receipt/<int:pk>/delete/', ReceiptDeleteView.as_view(), name='receipt-delete'),
]
