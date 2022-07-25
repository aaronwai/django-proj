from django.shortcuts import get_object_or_404, render
# import the 404 as well
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# choices at the same folder
from .choices import price_choices, state_choices, bedroom_choices
# load database into view
from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

# add additional parameter listing_id route


def listing(request, listing_id):
    # get an id or return 404
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords search, step 1 make sure no empty strings
    # step 2 then look up the keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                desciption__icontains=keywords)
    # second search field City, need to be exact but case insensitive
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)
    # add state search
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                city__iexact=state)
    # search bedrooms with less than option
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)
    # search price less than
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)
    # keep request object values
    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        "bedroom_choices": bedroom_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
