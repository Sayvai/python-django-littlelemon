from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Booking


class BookingTest(TestCase):
    # create a mock booking object, and ensure that the string (__str__) representation of the object is correct
    def test_get_item(self):
        user = User.objects.create(username="John Doe")
        booking = Booking.objects.create(
            user=user, no_of_guests=2, booking_date="2021-01-01 12:00:00"
        )
        self.assertEqual(str(booking), "John Doe : 2021-01-01 12:00:00 - 2 guest(s)")
