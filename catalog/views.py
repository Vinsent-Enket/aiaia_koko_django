from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(request, 'catalog/index.html')


def catalog(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/catalog.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_details(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'object': product
    }
    return render(request, 'catalog/product_details.html', context)
# Create your views here.
