# Generated by Django 3.1.5 on 2023-02-10 04:30

import archives.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0004_auto_20230209_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='pushnotification',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=archives.models.pushnotification_image_upload_url, verbose_name='이미지'),
        ),
    ]
