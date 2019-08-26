from django.shortcuts import render
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404



def main(request):
    title = 'главная'

    ProductCategories = ProductCategory.objects.all()
    basket = None

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content = {'title': title,
               'productcategories': ProductCategories,
               'basket': basket
    }

    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'продукты'
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is None:
        hot_product = Product.objects.filter(is_hot=True).first()
        content = {'title': title,
                   'hot_product': hot_product,
                   'categories': ProductCategory.objects.all(),
                   'basket': basket,

        }
        return render(request, 'mainapp/hot_product.html', content)
    else:
        products = Product.objects.all()
        if pk != 0:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = products.filter(category__pk=pk).order_by('price')

    content = {'title': title,
               'products': products,
               'categories': ProductCategory.objects.all(),
               'basket': basket,

    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукты'
    basket = None
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': basket,
    }

    return render(request, 'mainapp/product.html', content)

def contact(request):
    title = 'контакты'

    content = {'title': title}

    return render(request, 'mainapp/contact.html', content)