from django.shortcuts import render
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.shortcuts import get_object_or_404


def main(request):
    title = 'главная'

    ProductCategories = ProductCategory.objects.all()

    content = {'title': title, 'productcategories': ProductCategories}

    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    title = 'продукты'
    product_list = Product.objects.all()
    if pk:
        product_list = product_list.filter(category__pk=pk).order_by('price')


    content = {
        'title': title,
        'products': product_list,
        'categories': ProductCategory.objects.all(),
        'basket': basket,

    }

    return render(request, 'mainapp/products_list.html', content)



def contact(request):
    title = 'контакты'

    content = {'title': title}

    return render(request, 'mainapp/contact.html', content)