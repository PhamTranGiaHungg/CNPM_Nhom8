from django.contrib import admin
from .models import *

# Register your models here.
# Register Customer model to the Django Admin
# admin.site.register(Customer)

# Register Product model to the Django Admin
admin.site.register(Product)

admin.site.register(Category)

# Register Order model to the Django Admin
admin.site.register(Order)

# Register OrderItem model to the Django Admin
admin.site.register(OrderItem)

# Register ShippingAddress model to the Django Admin
admin.site.register(ShippingAddress)
