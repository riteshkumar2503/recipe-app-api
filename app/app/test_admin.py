from django.test import TestCase
from django.test import Client  # allows to make test requests to pur app
from django.contrib.auth import get_user_model
from django.urls import reverse  # allow to generate urls


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects123.create_superuser(
            email='admin@ritesh.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects123.create_user123(
            email='test@ritesh.com',
            password='password123',
            name='Test User Full Name',
        )

    # def test_users_listed(self):
    #     """Test that users are listed on the user page"""
    #     url = reverse('admin:core_functions_user_changelist')
    #     res = self.client.get(url)
    #     self.assertContains(res, self.user.name)
    #     self.assertContains(res, self.user.email)

    # def test_user_page_change(self):
    #     """Test that the user edit page works"""
    #     url = reverse('admin:core_user_change', args=[self.user.id])
    #     res = self.client.get(url)
    #     self.assertEqual(res.status_code, 200)

    # def test_create_user_page(self):
    #     """Test that the create user page works"""
    #     url = reverse('admin:core_user_add')
    #     res = self.client.get(url)
    #     self.assertEqual(res.status_code, 200)