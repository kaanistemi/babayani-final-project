from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import *
from checkout.models import *
from home.models import *
from .forms import ProductForm

# Create your views here.
all_coupon = Coupon.objects.filter(active=True)


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    all_coupons = Coupon.objects.filter(active=True)
    heading1 = 'We’re all about quality – and'
    heading2 = '100% solid hardwood'
    page_text = ' With the right care and attention – detailed in our Owner’s Manual – you’ll find that furniture made from hardwood just gets better with age. Our designs show off the natural beauty of oak and mango. Natural wood grains are unique to the piece of wood used in any given piece of furniture. Mango also has a striking range of colour, from light golds to darkest brown. You’ll find 100% solid hardwood underneath our painted finishes, too. We use a particular kind that gives the smoothest surface for the best finish.'

    #paget_text = PageText.objects.get(page="All Prducts").page_text

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            try:
                page = PageText.objects.get(page=categories[0])
                heading1 = page.heading1
                heading2 = page.heading2
                page_text = page.page_text
            except:
                heading1 = "NO HEADING1"
                heading2 = "NO HEADING2"
                page_text = 'NO TEXT FOUND'

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    coupon_code = None
    discount_percentage = 0
    if all_coupons.exists():
        coupon = all_coupons.first()
        coupon_code = coupon.code
        discount_percentage = coupon.discount_percentage

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'heading1': heading1,
        'heading2': heading2,
        'page_text': page_text,
        'coupon_code': coupon_code,
        'discount_percentage': discount_percentage
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        comment_obj = Comment()
        comment_obj.user = request.user
        comment_obj.product = product

        comment_obj.comment = request.POST['com']
        total_comments = product.total_comments
        Product.objects.filter(pk=product_id).update(
            total_comments=total_comments + 1)

        comment_obj.save()
    try:
        all_comments = Comment.objects.filter(product=product)
        total_comments = len(all_comments)
    except:
        total_comments = 0

    all_coupons = Coupon.objects.filter(active=True)
    coupon_code = None
    discount_percentage = 0
    if all_coupons.exists():
        coupon = all_coupons.first()
        coupon_code = coupon.code
        discount_percentage = coupon.discount_percentage

    context = {
        'product_id': product_id,
        'product': product,
        'all_comments': all_comments,
        'total_comments': total_comments,
        'coupon_code': coupon_code,
        'discount_percentage': discount_percentage,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    all_coupons = Coupon.objects.filter(active=True)
    coupon_code = None
    discount_percentage = 0
    if all_coupons.exists():
        coupon = all_coupons.first()
        coupon_code = coupon.code
        discount_percentage = coupon.discount_percentage

    template = 'products/add_product.html'
    context = {
        'form': form,
        'coupon_code': coupon_code,
        'discount_percentage': discount_percentage,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    all_coupons = Coupon.objects.filter(active=True)
    coupon_code = None
    discount_percentage = 0
    if all_coupons.exists():
        coupon = all_coupons.first()
        coupon_code = coupon.code
        discount_percentage = coupon.discount_percentage

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'coupon_code': coupon_code,
        'discount_percentage': discount_percentage,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
