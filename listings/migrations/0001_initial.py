# Generated by Django 5.1.5 on 2025-01-28 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('daire', 'Daire'), ('arsa', 'Arsa'), ('tarla', 'Tarla'), ('otel', 'Otel'), ('diğer', 'Diğer')], max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('listing_creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('satilik', 'Satılık'), ('kiralik', 'Kiralık')], default='satilik', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='listing_images/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listings.listing')),
            ],
        ),
    ]
