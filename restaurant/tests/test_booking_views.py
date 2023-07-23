from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from restaurant.models import Booking


class BookingViewTest(TestCase):
    # Use the setup() method to mock user authentication on the auth protected API, and create a couple of test instances of the Booking model, which will be used in the subsequent tests
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        Booking.objects.create(
            name="John Doe", no_of_guests=2, booking_date="2023-07-24 12:00:00"
        )
        Booking.objects.create(
            name="Jane Doe", no_of_guests=4, booking_date="2021-07-25 12:00:00"
        )

    # test: simulate URL dispatch call which maps (routes) to the Booking view, to then retrieve all the Booking objects (already mocked in setUp function above).
    # The retrieved Booking model objects should already be serialized by the view, where we just run assertions to check if the serialized data equals the response.
    def test_getall(self):
        response = self.client.get(
            "/restaurant/booking/table", follow=True
        )  # follow=True to ensure that the redirect is followed, since the Booking view is using ViewSet, and so the DefaultRouter needs to be used in the urls.py file, which routes booking/ to booking/table/

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]["name"], "John Doe")
        self.assertEqual(response.data[0]["no_of_guests"], 2)
        self.assertEqual(response.data[0]["booking_date"], "2023-07-24T12:00:00Z")

        self.assertEqual(response.data[1]["name"], "Jane Doe")
        self.assertEqual(response.data[1]["no_of_guests"], 4)
        self.assertEqual(response.data[1]["booking_date"], "2021-07-25T12:00:00Z")
