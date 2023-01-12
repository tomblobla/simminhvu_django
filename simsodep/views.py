from django.shortcuts import render
from store.models import Product, Tag, Category
from store.serializers import ProductSerializer, TagSerializer, CategorySerializer


def home(request):
    products = Product.objects.all().filter(
        is_available=True,
        sale_off__gt=0
    )
    productsSerializer = ProductSerializer(
        products.order_by("-id")[:9], many=True)
    
    context = {
        'products': productsSerializer.data,
        'tags': TagSerializer(Tag.objects.all(), many=True).data,
        'categories': CategorySerializer(Category.objects.all(), many=True).data,
    }

    return render(request, 'home.html', context)
