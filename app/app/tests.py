from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """
        Test that two numbers are added together
        :return:
        """
        self.assertEqual(add(3, 8), 11)

    def test_subtruct_numbers(self):
        """
        Test that values are subtracted and result is returned
        :return:
        """
        self.assertEqual(subtract(5, 11), -6)
