from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    title = 'главная'

    ProductCategories = ProductCategory.objects.all()

    content = {'title': title, 'productcategories': ProductCategories}

    return render(request, 'mainapp/index.html', content)


def products(request):
    title = 'продукты'

    products = Product.objects.all()

    content = {'title': title, 'products': products}

    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'контакты'

    content = {'title': title}

    return render(request, 'mainapp/contact.html', content)
