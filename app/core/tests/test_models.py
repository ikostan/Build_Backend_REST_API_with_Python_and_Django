from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import MESSAGES


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        # Arrange
        email = "test@testemail.com"
        password = 'password123'
        # Act
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        # Assert
        # compare emails
        self.assertEqual(user.email, email)
        # compare passwords
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the mmail for a new user is normalized"""
        # Arrange
        email = "tEst@teStemaiL.cOM"
        # Act
        user = get_user_model().objects.create_user(
            email=email,
            password='password123'
        )
        # Assert
        self.assertEqual(user.email, 'tEst@testemail.com')

    def test_new_user_invalid_email(self):
        """Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            # Arrange & Act
            get_user_model().objects.create_user(
                email=None,
                password='password123'
            )

    def test_invalid_email_error(self):
        """Verify 'invalid_email' error"""
        # Arrange & Act
        try:
            get_user_model().objects.create_user(
                    email=None,
                    password='password123'
            )
        except ValueError as e:
            self.assertEqual(e.__str__(), MESSAGES['invalid_email'])

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='superuser@test.com',
            password='password123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
