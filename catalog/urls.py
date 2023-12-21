from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, catalog, contacts

app_name = CatalogConfig.name


urlpatterns = [
    path('', index, name='index'),
    path('catalog', catalog, name='catalog'),
    path('contacts', contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
