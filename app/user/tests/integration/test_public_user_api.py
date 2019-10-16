from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class PublicUserApiTest(TestCase):
    """
    Testing Public User API
    """

    @classmethod
    def setUpClass(cls):

        cls.CREATE_USER_URL = reverse('user:create')

    def setUp(self) -> None:

        self.client = APIClient()

    @staticmethod
    def create_user(**params):
        """
        Create user helper function
        :param params:
        :return:
        """
        return get_user_model().objects.create_user(**params)

    def test_create_valid_user_success(self):
        """
        Test creating user with valid
        payload is successful
        :return:
        """

        # user data
        payload = {
            'email': 'test@test.com',
            'password': 'password12345',
            'name': 'Test User'
        }
        # create user by sending HTTP POST request
        res = self.client.post(self.CREATE_USER_URL,
                               payload)
        # verify status code
        self.assertEqual(res.status_code,
                         status.HTTP_201_CREATED)
        # get user model from the system
        # verify that new user object created
        user = get_user_model().objects.get(**res.data)
        # verify user password
        self.assertTrue(user.check_password(payload['password']))
        # verify that user password is not send in server response
        self.assertNotIn('password', res.data)

    def test_create_user_already_exists(self):
        """
        Test creating user when
        same user already exist
        :return:
        """
        # user data
        payload = {
            'email': 'test@test.com',
            'password': 'password12345',
            'name': 'Test User'
        }
        # create user
        self.create_user(**payload)
        # try to create duplicate user by
        # sending HTTP POST request
        res = self.client.post(self.CREATE_USER_URL,
                               payload)
        # verify status code
        self.assertEqual(res.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_create_user_pwd_too_short(self):
        """
        Test creating user when
        password is too short
        (password length less that 6 chars)
        :return:
        """
        payload = {
            'email': 'test@test.com',
            'password': 'pwd12',
            'name': 'Test User'
        }
        # create user by sending HTTP POST request
        res = self.client.post(self.CREATE_USER_URL,
                               payload)
        # verify status code
        self.assertEqual(res.status_code,
                         status.HTTP_400_BAD_REQUEST)
        # verify that user wasn't created
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
