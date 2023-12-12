from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Receipt

class ReceiptViewTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='123')
        self.client.login(username='testuser', password='123')

        # Create a receipt
        self.receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            purchase_date='2021-01-01',
            item_list='Item1, Item2',
            total_amount=100.00
        )

    def test_receipt_list_view(self):
        response = self.client.get(reverse('receipt-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipts/list.html')
        self.assertContains(response, 'Test Store')

    def test_receipt_detail_view(self):
        response = self.client.get(reverse('receipt-detail', args=[self.receipt.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipts/detail.html')

    def test_receipt_create_view(self):
        response = self.client.post(reverse('receipt-create'), {
            'store_name': 'New Store',
            'purchase_date': '2021-02-01',
            'item_list': 'Item3, Item4',
            'total_amount': 150.00
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(Receipt.objects.filter(store_name='New Store').exists())

    def test_receipt_update_view(self):
        response = self.client.post(reverse('receipt-update', args=[self.receipt.id]), {
            'store_name': 'Updated Store',
            'purchase_date': '2021-01-01',
            'item_list': 'Item1, Item2',
            'total_amount': 100.00
        })
        self.receipt.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.receipt.store_name, 'Updated Store')

    def test_receipt_delete_view(self):
        response = self.client.post(reverse('receipt-delete', args=[self.receipt.id]))
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertFalse(Receipt.objects.filter(id=self.receipt.id).exists())



class AuthViewTests(TestCase):

    def test_login_view(self):
        # Create a test user
        User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        # Test login
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, expected_url=reverse('receipt-list'), status_code=302, target_status_code=200)

    def test_signup_view(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertRedirects(response, expected_url=reverse('login'), status_code=302, target_status_code=200)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_access_protected_view_unauthenticated(self):
        response = self.client.get(reverse('receipt-create'))
        self.assertRedirects(response, expected_url='/login/?next=/receipt/new/', status_code=302, target_status_code=200)