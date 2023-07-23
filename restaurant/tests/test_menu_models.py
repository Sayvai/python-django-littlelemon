from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    # create a mock menu object, and ensure that the string (__str__) representation of the object is correct
    def test_get_item(self):
        menu = Menu.objects.create(title="Test menu item", price=10.00, inventory=10)
        self.assertEqual(str(menu), "Test menu item : 10.00")
