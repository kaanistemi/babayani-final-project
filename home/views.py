from django.shortcuts import render
from products.models import *
from checkout.models import *
# Create your views here.


def index(request):
    """ Return to index page """
    category = None
    categoryQS = Category.objects.filter(name='new_arrivals')
    if categoryQS.exists():
        category = categoryQS.first()

    products = None
    if category:
        products = Product.objects.filter(category=category)

    coupon = None
    coupon_code = None
    discount_percentage = None
    couponQS = Coupon.objects.filter(active=True)
    if couponQS.exists():
        coupon = couponQS.first()

    if coupon:
        coupon_code = coupon.code
        discount_percentage = coupon.discount_percentage

    context = {
        'coupon_code': coupon_code,
        'discount_percentage': discount_percentage,
        'products': products
    }

    return render(request, 'home/index.html', context)
