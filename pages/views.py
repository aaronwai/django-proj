from django.shortcuts import render
from django.http import HttpResponse
# import dictionary for choices
from listings.choices import price_choices, state_choices, bedroom_choices
# create a function for for the index link to urls API route
from listings.models import Listing

# about page is mainly realtor=, so import realtor model
from realtors.models import Realtor


def index(request):
    # show 3 listing only
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    # add choices into the object
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        "bedroom_choices": bedroom_choices
    }
    return render(request, "pages/index.html", context)


def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # get MVP, which is only one
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, "pages/about.html", context)
