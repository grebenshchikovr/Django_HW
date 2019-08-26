from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def basket(request):
    basket = None
    if request.user.is_authenticated:
        basket = request.user.basket.all()
    return render(request, 'basketapp/basket.html', {'basket_items': basket})

@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.is_authenticated:
        basket = request.user.basket.filter(product=product).first()
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk):
    basket = get_object_or_404(Basket, pk=pk)

    quantity = int(request.GET.get('quantity'))
    if quantity > 0:
        basket.quantity = quantity
        basket.save()
    else:
        basket.delete()
    return HttpResponse('OK')