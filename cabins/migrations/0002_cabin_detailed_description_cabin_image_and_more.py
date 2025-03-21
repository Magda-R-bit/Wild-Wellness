# Generated by Django 5.1.5 on 2025-02-08 18:15

import django_resized.forms
import djrichtextfield.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cabins", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cabin",
            name="detailed_description",
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="cabin",
            name="image",
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format="WEBP",
                keep_meta=True,
                null=True,
                quality=80,
                scale=None,
                size=[600, None],
                upload_to="cabins/",
            ),
        ),
        migrations.AddField(
            model_name="cabin",
            name="image_alt",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="cabin",
            name="max_guests",
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name="cabin",
            name="short_description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
