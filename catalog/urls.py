from django.urls import path

from catalog.views import index, catalog, contacts

urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('contacts', contacts)
]