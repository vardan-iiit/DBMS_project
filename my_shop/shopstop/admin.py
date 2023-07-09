from django.contrib import admin
from .models import Customer,Product,PhoneNumber,Cart,InCartProducts,Seller,ShippingAddress,ProductStock,Category,Orders,Payments,ProductDescriptors,DatabaseAdministrator,TrackingAndCancellation
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(PhoneNumber)
admin.site.register(Cart)
admin.site.register(InCartProducts)
admin.site.register(Seller)
admin.site.register(ShippingAddress)
admin.site.register(ProductStock)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Payments)
admin.site.register(ProductDescriptors)
admin.site.register(DatabaseAdministrator)
admin.site.register(TrackingAndCancellation)

