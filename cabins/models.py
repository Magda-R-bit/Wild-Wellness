from django.db import models

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from cloudinary_storage.storage import MediaCloudinaryStorage



class Cabin(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    detailed_description = RichTextField(null=True, blank=True)
    
    image = ResizedImageField(size=[600, 335], storage=MediaCloudinaryStorage(), upload_to="cabins/", force_format="WEBP", quality=80, blank=False, null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    bedroom_image = ResizedImageField(size=[350, 200], storage=MediaCloudinaryStorage(), upload_to="cabins/bedroom/", force_format="WEBP", quality=80, blank=True, null=True)
    bathroom_image = ResizedImageField(size=[350, 200], storage=MediaCloudinaryStorage(), upload_to="cabins/bathroom/", force_format="WEBP", quality=80, blank=True, null=True)
    kitchen_image = ResizedImageField(size=[350, 200], storage=MediaCloudinaryStorage(), upload_to="cabins/kitchen/", force_format="WEBP", quality=80, blank=True, null=True)
    
    location = models.CharField(max_length=200)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.IntegerField(default=4)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
