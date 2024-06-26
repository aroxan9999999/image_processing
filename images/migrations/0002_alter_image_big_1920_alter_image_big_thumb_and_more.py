# Generated by Django 5.0.6 on 2024-06-25 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='big_1920',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='big_thumb',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='d2500',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='original',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
