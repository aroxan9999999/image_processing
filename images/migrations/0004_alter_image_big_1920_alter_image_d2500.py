# Generated by Django 5.0.6 on 2024-06-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_big_1920_alter_image_big_thumb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='big_1920',
            field=models.ImageField(blank=True, null=True, upload_to='big_1920/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='d2500',
            field=models.ImageField(blank=True, null=True, upload_to='d2500/'),
        ),
    ]
