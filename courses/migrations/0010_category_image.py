# Generated by Django 5.1.6 on 2025-05-05 00:41

import cloudinary.models
import django.utils.timezone
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_courseimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
