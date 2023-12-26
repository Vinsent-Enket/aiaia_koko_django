from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, CatalogListView, ProductDetailView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog_of_products', CatalogListView.as_view(), name='catalog_of_products'),
    path('contacts', contacts, name='contacts'),
    path('product_details/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_details/<int:pk>/', BlogDetailView.as_view(), name='blog_details'),
    path('blog_edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

]
