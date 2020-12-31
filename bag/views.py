from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import *
from products.models import Product
from checkout.models import *
from bag.context import bag_contents
from django.conf import settings

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    coupon = None
    all_coupon = Coupon.objects.filter(active=True)

    if all_coupon.exists():
        coupon = all_coupon.first()

    coupon_code = None
    discount_percentage = 0
    if coupon:
        coupon_code = coupon.code
        discount_percentage = coupon.discount_percentage

    used_status = True
    try:
        all_used_coupon = Used_coupon.objects.filter(user=request.user)
        if len(all_used_coupon) < 1:
            used_status = False
    except:
        pass

    context = {
        'coupon_code': coupon_code,
        'discount_percentage': discount_percentage,
        'used_status': used_status,
        'discount': 00
    }

    if request.method == 'POST' and 'coupon_applied' in request.POST:

        current_bag = bag_contents(request)
        print('=====================new request===================')
        print(current_bag)
        coupon = request.POST['coupon']
        coupon_obj = Coupon.objects.get(code=coupon)

        coupon_discount = int(int(current_bag['total']) * .1)
        settings.DISCOUNT = coupon_discount
        print("coupon_discount: ", coupon_discount)
        current_bag[
            'grand_total'] = current_bag['grand_total'] - coupon_discount

        print(current_bag['grand_total'])
        print(current_bag)

        request.session.modified = True

        used_coupon = Used_coupon()
        used_coupon.user = request.user
        used_coupon.coupon = coupon_obj
        used_coupon.save()

        context['used_status'] = True
        context['discount'] = coupon_discount

        return render(request, 'bag.html', context=context)

    return render(request, 'bag.html', context=context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if request.user.is_authenticated:
        bag_obj = Bag()
        bag_obj.user = request.user
        bag_obj.item = product
        bag_obj.quantity = quantity
        bag_obj.save()

        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             f'Updated {product.name} to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag! ')

            request.session['bag'] = bag

    else:

        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             f'Updated {product.name} to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag! ')

            request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag! ')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_to_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        info = None
        if 'product_info' in request.POST:
            size = request.POST['product_info']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_info'][info]
            if not bag[item_id]['items_by_info']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

        
