"""
URL configuration for emlak_sitesi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.urls import path
from listings import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),
    path('', views.home, name='home'),

    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('add-listing/', views.add_listing, name='add_listing'),
    path('kiralik/<int:pk>/', views.ev_detail, name='ev_detail'),
    path('kiralik/', views.kiralik, name='kiralik'),
    path('satilik/<int:pk>/', views.ev_detail, name='ev_detail'),
    path('satilik/', views.satilik, name='satilik'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
                  path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
                  path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
                       name='password_reset_confirm'),
                  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
                       name='password_reset_complete'),

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)