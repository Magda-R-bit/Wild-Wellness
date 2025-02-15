from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.check_in>= self.check_out:
            raise ValueError("Check out date must be after the check-in date.")
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"Booking by {self.user.username} for {self.item_name} from {self.check_in} to {self.check_out}"