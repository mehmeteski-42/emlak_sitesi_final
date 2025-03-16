from django.urls import path
from .views import ListingList
from .views import ListingDetail
from .views import ListingCreate, ListingUpdate
from . import views
from django.urls import path



urlpatterns = [
    path('listings/', ListingList.as_view(), name='listing-list'),
    path('listings/', ListingList.as_view(), name='listing-list'),
    path('listings/<int:pk>/', ListingDetail.as_view(), name='listing-detail'),
    path('listings/', ListingList.as_view(), name='listing-list'),
    path('listings/<int:pk>/', ListingDetail.as_view(), name='listing-detail'),
    path('listings/create/', ListingCreate.as_view(), name='listing-create'),
    path('listings/update/<int:pk>/', ListingUpdate.as_view(), name='listing-update'),
    path('search/', views.search_view, name='search'),

]

