from django.test import TestCase
from app.calc import add
from app.calc import sub
from django.contrib.auth import get_user_model



class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        self.assertEqual(sub(23, 5), 18)



class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@ritesh.com'
        password = 'Password123'
        user = get_user_model().objects123.create_user123(email=email, password=password)
        print("aaa", user)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@RITESH.COM'
        user = get_user_model().objects123.create_user123(email=email, password="passxyz")
        print("bbb", user.__dict__)
        self.assertEqual(user.email, email.lower())

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects123.create_superuser('test@ritesh.com','test123')
        print("ccc", user.__dict__)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


