from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from cabins.models import Cabin
from .models import Booking
import datetime
from datetime import date, timedelta
from booking.forms import BookingForm
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.cabin = Cabin.objects.create(
            name="Test Cabin", price_per_night=100, is_available=True
        )
        self.booking = Booking.objects.create(
            user=self.user,
            cabin=self.cabin,
            check_in=datetime.date.today(),
            check_out=datetime.date.today() + datetime.timedelta(days=2),
        )

    def test_booking_total_price(self):
        self.assertEqual(self.booking.total_price, 200)

    def test_booking_string_representation(self):
        expected_str = (
            f"Booking by {self.user.username} for {self.cabin.name} "
            f"from {self.booking.check_in} to {self.booking.check_out}"
        )
        self.assertEqual(str(self.booking), expected_str)


class BookingFormTest(TestCase):
    def setUp(self):
        """Set up a test cabin for booking form tests."""
        self.cabin = Cabin.objects.create(
            name="Test Cabin", price_per_night=100
        )

    def test_booking_form_valid(self):
        """Test if the form correctly accepts valid dates."""
        valid_data = {
            "cabin": self.cabin.id,
            "check_in": date.today() + timedelta(days=1),  # Future date
            "check_out": date.today() + timedelta(days=5),  # After check-in
        }
        valid_form = BookingForm(data=valid_data)
        self.assertTrue(valid_form.is_valid())  # Expecting True

    def test_booking_form_invalid_dates(self):
        """Test if the form correctly rejects past
        check-in and invalid check-out dates."""

        #  Case 1: Check-in date in the past
        past_date_data = {
            "cabin": self.cabin.id,
            "check_in": date.today() - timedelta(days=1),  # Past date
            "check_out": date.today() + timedelta(days=2),
        }
        past_date_form = BookingForm(data=past_date_data)
        self.assertFalse(past_date_form.is_valid())

        self.assertIn(
            "__all__", past_date_form.errors
        )  # Check form-wide error
        self.assertIn(
            "⚠️ Check-in date cannot be in the past!",
            past_date_form.errors["__all__"],
        )

        # Case 2: Check-out date before check-in
        invalid_range_data = {
            "cabin": self.cabin.id,
            "check_in": date.today() + timedelta(days=3),
            "check_out": date.today() + timedelta(days=2),  # Before check-in
        }
        invalid_range_form = BookingForm(data=invalid_range_data)
        self.assertFalse(invalid_range_form.is_valid())

        self.assertIn(
            "__all__", invalid_range_form.errors
        )  # Check form-wide validation
        self.assertIn(
            "⚠️ Check-out date must be after check-in.",
            invalid_range_form.errors["__all__"],
        )


class BookingViewsTest(TestCase):
    def setUp(self):
        """Set up user, cabin with image, and booking."""
        self.user = User.objects.create_user(
            username="testuser", password="password"
        )
        self.client.login(username="testuser", password="password")

        # Create a mock image for the cabin
        self.cabin = self._create_cabin_with_image()

        # Create a booking
        self.booking = Booking.objects.create(
            user=self.user,
            cabin=self.cabin,
            check_in=datetime.date.today() + datetime.timedelta(days=1),
            check_out=datetime.date.today() + datetime.timedelta(days=3),
        )

    def _create_cabin_with_image(self):
        """Helper function to create a cabin with an image."""
        image = Image.new(
            "RGB", (600, 335), color=(255, 0, 0)
        )  # Create a red image
        image_io = BytesIO()
        image.save(image_io, format="PNG")
        image_io.seek(0)
        mock_image = SimpleUploadedFile(
            "test_image.png", image_io.read(), content_type="image/png"
        )

        cabin = Cabin.objects.create(
            name="Test Cabin", price_per_night=100, is_available=True
        )
        cabin.image.save(
            "test_image.png", mock_image
        )  # Save the image to the cabin
        return cabin

    def test_booking_list_view(self):
        """Test that the booking list view displays the cabin image."""
        response = self.client.get(reverse("booking_list"))
        self.assertEqual(response.status_code, 200)

        # Check if the cabin image is rendered (using the image URL)
        self.assertContains(
            response, "https://res.cloudinary.com/drrjh78y3/image/upload"
        )

    def test_booking_create_view(self):
        """Test the booking creation page."""
        response = self.client.get(reverse("booking_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create Booking")

    def test_booking_update_view(self):
        """Test the booking update page."""
        response = self.client.get(
            reverse("booking_update", args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_booking_delete_view(self):
        """Test the booking deletion process."""
        response = self.client.post(
            reverse("booking_delete", args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 302)  # Redirects after success
