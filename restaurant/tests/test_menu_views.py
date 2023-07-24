from django.test import TestCase

from restaurant.models import Menu


class MenuViewTest(TestCase):
    # Use the setup() method to create a few test instances of the Menu model, which will be used in the subsequent tests
    def setUp(self):
        Menu.objects.create(title="Test menu item", price=10.00, inventory=10)
        Menu.objects.create(title="Test menu item 2", price=20.00, inventory=20)
        Menu.objects.create(title="Test menu item 3", price=30.00, inventory=30)

    # test: simulate URL dispatch call which maps (routes) to the Menu view, to then retrieve all the Menu objects (already mocked in setUp function above).
    # The retrieved Menu model objects should already be serialized by the view, where we just run assertions to check if the serialized data equals the response.
    def test_getall(self):
        response = self.client.get("/restaurant/menu")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

        self.assertEqual(response.data[0]["title"], "Test menu item")
        self.assertEqual(response.data[0]["price"], "10.00")
        self.assertEqual(response.data[0]["inventory"], 10)

        self.assertEqual(response.data[1]["title"], "Test menu item 2")
        self.assertEqual(response.data[1]["price"], "20.00")
        self.assertEqual(response.data[1]["inventory"], 20)

        self.assertEqual(response.data[2]["title"], "Test menu item 3")
        self.assertEqual(response.data[2]["price"], "30.00")
        self.assertEqual(response.data[2]["inventory"], 30)
