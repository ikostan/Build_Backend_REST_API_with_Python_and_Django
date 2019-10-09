from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self) -> None:
        """
        Set Up function.
        Runs before every test
        :return:
        """

        # Create admin user and force login
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@test.com',
            password='admin12345'
        )
        self.client.force_login(self.admin_user)

        # Create non admin user
        self.user = get_user_model().objects.create_user(
            email='user@test.com',
            password='user12345',
            name="Test User"
        )

    def test_users_listed(self):
        """
        Test that users are listed on user page
        :return:
        """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
