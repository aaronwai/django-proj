from django.urls import path
from . import views
# set the / api, as variable=index to callback function
# /listings/   all the listings api
urlpatterns = [
    path('', views.index, name="listings"),
    path('<int:listing_id>', views.listing, name="listing"),
    path('search', views.search, name="search")
]
