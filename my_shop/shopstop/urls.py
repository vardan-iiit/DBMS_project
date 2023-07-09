from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="shophome"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="ContactUs"),
    path('tracker/',views.tracker,name="TrackingStatus"),
    path('search/',views.search,name="Search"),
    path('productview/',views.proview,name="proview"),
    path('checkout',views.checkout,name="Checkout"),
    path('addtocart',views.addtocart,name="addtocart"),
    path('viewcart',views.viewcart,name="viewcart"),
    path('placeorder',views.placeorder,name="placeorder")
    
]
