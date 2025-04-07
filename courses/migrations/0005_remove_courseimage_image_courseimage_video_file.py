# Generated by Django 5.2 on 2025-04-07 00:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_category_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseimage',
            name='image',
        ),
        migrations.AddField(
            model_name='courseimage',
            name='video_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='videos/'),
            preserve_default=False,
        ),
    ]
