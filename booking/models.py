from django.db import models
from django.contrib.auth.models import User
from cabins.models import Cabin


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    cabin = models.ForeignKey(
        Cabin, on_delete=models.CASCADE, related_name="bookings"
    )
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        nights = (self.check_out - self.check_in).days
        if nights > 0:
            self.total_price = self.cabin.price_per_night * nights
        else:
            self.total_price = 0  # Prevents negative pricing errors
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Booking by {self.user.username} for {self.cabin.name} "
            f"from {self.check_in} to {self.check_out}"
        )
