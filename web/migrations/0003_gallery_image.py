# Generated by Django 3.2.9 on 2021-12-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_image_gallery_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='gallery/'),
        ),
    ]
