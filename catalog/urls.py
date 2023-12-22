from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, catalog, contacts, product_details

app_name = CatalogConfig.name

urlpatterns = [
                  path('', index, name='index'),
                  path('catalog', catalog, name='catalog'),
                  path('contacts', contacts, name='contacts'),
                  path('product_details', product_details, name='product_details'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
