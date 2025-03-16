from django.db import models

# Listing Model
class Listing(models.Model):
    PROPERTY_TYPES = [
        ('daire', 'Daire'),
        ('arsa', 'Arsa'),
        ('tarla', 'Tarla'),
        ('otel', 'Otel'),
        ('diğer', 'Diğer')
    ]

    # For Sale or For Rent status
    LISTING_STATUS = [
        ('satilik', 'Satılık'),  # For Sale
        ('kiralik', 'Kiralık'),  # For Rent
    ]


    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Yeni alan: Metrekare
    area = models.IntegerField(null=True, blank=True)  # Metrekare alanı ekliyoruz

    # Yeni alan: İlanın eklenme tarihi (varsa ayrıca bir tarih eklemek)
    listing_creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # İlanın eklenme tarihi ekliyoruz

    # New field to specify the listing's status (For Sale or For Rent)
    status = models.CharField(max_length=10, choices=LISTING_STATUS, default='satilik')

    def __str__(self):
        return self.title

# ListingImage Model
class ListingImage(models.Model):
    image = models.ImageField(upload_to='listing_images/')
    caption = models.CharField(blank=True, max_length=255)
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE, related_name='images')


    def __str__(self):
        return f"{self.listing.title} - Image"

