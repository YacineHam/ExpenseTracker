from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    purchase_date = models.DateField()
    item_list = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.store_name} on {self.purchase_date}"