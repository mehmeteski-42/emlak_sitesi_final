
from django.contrib import admin
from .models import Listing, ListingImage

# Listing ve ListingImage modellerini admin paneline kaydediyoruz.
class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1  # Yeni resim eklemek için ek alan sayısı

class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageInline]  # Listing'e resim eklemek için ListingImageInline ekliyoruz

admin.site.register(Listing, ListingAdmin)

# User modelini admin paneline kaydediyoruz

