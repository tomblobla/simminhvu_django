from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Tag, Category, Order
from .serializers import ProductSerializer, TagSerializer, CategorySerializer
# Create your views here.


def loai_sim(request, tag_slug):
    tags = None
    products = None

    if (tag_slug != None):
        tags = get_object_or_404(Tag, id=tag_slug)
        products = Product.objects.all().filter(tags=tags, is_available=True)
    else:
        products = Product.objects.all().filter(
            is_available=True).order_by('created_date')[:16]

    productsSerializer = ProductSerializer(products, many=True)

    productsSerializer = ProductSerializer(
        products, many=True)

    tagSerializer = TagSerializer(
        Tag.objects.all(), many=True)

    categorySerializer = CategorySerializer(Category.objects.all(), many=True)

    context = {
        "tags": tagSerializer.data,
        "products": productsSerializer.data,
        "categories": categorySerializer.data,
    }

    return render(request, 'shop.html', context)


def shop(request, category_slug=None):
    categories = None
    products = None

    if (category_slug != None):
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(
            is_available=True).order_by('created_date')[:16]

    productsSerializer = ProductSerializer(products, many=True)

    productsSerializer = ProductSerializer(
        products, many=True)

    tagSerializer = TagSerializer(
        Tag.objects.all(), many=True)

    categorySerializer = CategorySerializer(Category.objects.all(), many=True)

    context = {
        "tags": tagSerializer.data,
        "products": productsSerializer.data,
        "categories": categorySerializer.data,
    }

    return render(request, 'shop.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_prod = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    tagSerializer = TagSerializer(
        Tag.objects.all(), many=True)

    categorySerializer = CategorySerializer(Category.objects.all(), many=True)

    context = {
        "tags": tagSerializer.data,
        "single_prod": single_prod,
        "categories": categorySerializer.data,
    }
    return render(request, 'detailed_prod.html', context)


def order(request):
    if request.method == 'POST':
        product_id = request.POST.get('hiddenID')
        address = request.POST.get('address')
        print(address)
        if (request.user == None or address == None):
            return redirect('/accounts/login')
        # Do something with the data
        order = Order.objects.create(
            product_id=product_id, address=address, user=request.user)
        Product.objects.filter(id=product_id).update(is_available=False)
        order.save()
        # return render(request, 'confirmation.html', context={'order': order})
        return redirect('/shop')
    else:
        return redirect('/shop')
