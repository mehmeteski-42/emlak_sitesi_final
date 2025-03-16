from cgi import print_form

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.generics import RetrieveAPIView
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing


class ListingList(APIView):
    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

class ListingDetail(RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

# İlan Ekleme
class ListingCreate(CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]  # Sadece giriş yapmış kullanıcılar
    permission_classes = [IsAdminUser]

# İlan Güncelleme
class ListingUpdate(UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]  # Sadece giriş yapmış kullanıcılar
    permission_classes = [IsAdminUser]

def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listing_detail.html', {'listing': listing})

def search_view(request):
    query = request.GET.get('q')
    if query:
        results = Listing.objects.filter(name__icontains=query)

def contact(request):
    return render(request, 'contact.html')

def arsa(request):
    arsa_listesi = Listing.objects.filter(type='arsa')# 'kategori' field'ını arsa olanları alıyoruz
    return render(request, 'arsa.html', {'arsalar': arsa_listesi})

def ev(request):
    ev_listesi = Listing.objects.filter(type='ev')# 'kategori' field'ını arsa olanları alıyoruz
    return render(request, 'ev.html', {'evler': ev_listesi})

def tarla(request):
    tarla_listesi = Listing.objects.filter(type='tarla')
    return render(request, 'tarla.html', {'tarlalar': tarla_listesi})

def ev_detail(request, pk):
    # Ev id'sine göre ev objesini almak
    ev = get_object_or_404(Listing, pk=pk)
    return render(request, 'ev_detail.html', {'ev': ev})


def kiralik(request):
    # Başlangıçta tüm ilanları alıyoruz burayı kiralık diye değiştiririz sonradan
    listings = Listing.objects.filter(status='kiralik')

    # Filtreleme parametrelerini `GET` üzerinden alıyoruz
    property_type = request.GET.get('property_type', '')  # Tür
    min_price = request.GET.get('min_price', '')  # Min fiyat
    max_price = request.GET.get('max_price', '')  # Max fiyat

    # Filtreleme işlemleri
    if property_type:
        listings = listings.filter(type=property_type)

    if min_price:
        listings = listings.filter(price__gte=min_price)  # Min fiyat filtresi

    if max_price:
        listings = listings.filter(price__lte=max_price)  # Max fiyat filtresi

    # Filtrelenmiş ilanları template'e gönderiyoruz
    return render(request, 'kiralik.html', {
        'listings': listings,
        'property_type': property_type,
        'min_price': min_price,
        'max_price': max_price,
    })

def satilik(request):
    # Başlangıçta tüm ilanları alıyoruz burayı satılık diye değiştiririz
    listings = Listing.objects.filter(status='satilik')

    # Filtreleme parametrelerini `GET` üzerinden alıyoruz
    property_type = request.GET.get('property_type', '')  # Tür
    min_price = request.GET.get('min_price', '')  # Min fiyat
    max_price = request.GET.get('max_price', '')  # Max fiyat

    # Filtreleme işlemleri
    if property_type:
        listings = listings.filter(type=property_type)

    if min_price:
        listings = listings.filter(price__gte=min_price)  # Min fiyat filtresi

    if max_price:
        listings = listings.filter(price__lte=max_price)  # Max fiyat filtresi

    # Filtrelenmiş ilanları template'e gönderiyoruz
    return render(request, 'satilik.html', {
        'listings': listings,
        'property_type': property_type,
        'min_price': min_price,
        'max_price': max_price,
    })

def search(request):
    query = request.GET.get('q', '')  # Kullanıcıdan gelen arama kelimesi
    listings = Listing.objects.all()

    if query:
        listings = listings.filter(
            title__icontains=query  # Arama kelimesi başlıkta geçiyorsa
        ) | listings.filter(
            description__icontains=query  # Arama kelimesi açıklamada geçiyorsa
        ) | listings.filter(
            location__icontains=query  # Arama kelimesi konumda geçiyorsa
        )

    return render(request, 'search.html', {'listings': listings, 'query': query})

def add_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        type = request.POST['type']
        description = request.POST['description']
        contact_number = request.POST['contact_number']
        Listing.objects.create(
            title=title,
            price=price,
            type=type,
            description=description,
            contact_number=contact_number,
        )
        return redirect('home')
    return render(request, 'add_listing.html')