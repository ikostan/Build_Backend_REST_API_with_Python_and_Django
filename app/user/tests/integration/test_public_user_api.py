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
        # Fix for error:
        # AttributeError: type object 'PublicUserApiTest'
        # has no attribute 'cls_atomics'
        # Source: https://github.com/Microsoft/PTVS/issues/41
        super(PublicUserApiTest, cls).setUpClass()

        # The reverse() function can reverse a large
        # variety of regular expression patterns for URLs,
        # but not every possible one. The main restriction
        # at the moment is that the pattern cannot contain
        # alternative choices using the vertical bar ("|")
        # character. You can quite happily use such patterns
        # for matching against incoming URLs and sending them
        # off to views, but you cannot reverse such patterns.
        cls.CREATE_USER_URL = reverse('user:create')

        # URL TOKEN
        cls.TOKEN_URL = reverse('user:token')

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

    def test_create_token_for_user(self):
        """
        Test created token for the user
        :return:
        """
        # user data
        payload = {
            'email': 'test@test.com',
            'password': 'testpassword',
        }
        # create user
        self.create_user(**payload)
        # send login request
        res = self.client.post(self.TOKEN_URL, payload)
        # assert response code
        self.assertEqual(res.status_code,
                         status.HTTP_200_OK)
        # verify auth token
        self.assertIn('token', res.data)
        # verify that no password in response
        self.assertNotIn('password', res.data)

    def test_create_token_invalid_credentials(self):
        """
        Test that token is not created if invalid
        credentials are given
        :return:
        """

        self.create_user(email="test@test.com",
                         password="testpassword")
        payload = {'email': "test@test.com",
                   'password': "wrongpassword"}

        # send auth request
        res = self.client.post(self.TOKEN_URL,
                               payload)
        # verify response code
        self.assertEqual(res.status_code,
                         status.HTTP_400_BAD_REQUEST)
        # verify that token not in the response
        self.assertNotIn('token', res.data)
        # verify that no password in response
        self.assertNotIn('password', res.data)

    def test_create_token_user_does_not_exist(self):
        """
        Test that token is not created if
        user does not exist
        :return:
        """

        payload = {'email': "test@test.com",
                   'password': "wrongpassword"}

        # send auth request
        res = self.client.post(self.TOKEN_URL,
                               payload)
        # verify response code
        self.assertEqual(res.status_code,
                         status.HTTP_400_BAD_REQUEST)
        # verify that token not in the response
        self.assertNotIn('token', res.data)
        # verify that no password in response
        self.assertNotIn('password', res.data)

    def test_create_token_no_password(self):
        """
        Test that token is not created if invalid
        no password (empty password string) given
        :return:
        """

        self.create_user(email="test@test.com",
                         password="testpassword")
        payload = {'email': "test@test.com",
                   'password': ""}

        # send auth request
        res = self.client.post(self.TOKEN_URL,
                               payload)
        # verify response code
        self.assertEqual(res.status_code,
                         status.HTTP_400_BAD_REQUEST)
        # verify that token not in the response
        self.assertNotIn('token', res.data)
        # verify that no password in response
        self.assertNotIn('password', res.data)
