from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email is successful
        :return:
        """
        email = 'test@test.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized
        :return:
        """
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email=email, password='test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email creates an error
        :return:
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='test123')

    def test_create_new_super_user(self):
        """
        Test creating a new superuser
        :return:
        """
        user = get_user_model().objects.create_superuser(
            email='test@TEST.com',
            password='test12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
