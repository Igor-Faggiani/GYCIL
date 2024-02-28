# Generated by Django 5.0 on 2024-02-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='description',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='budget',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]