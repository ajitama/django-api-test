from django.contrib import admin
from coupon.models import Coupon


# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    list_display = (
            'request_code', 
            'url', 
            'arg1',
            'arg2',
            )

admin.site.register(Coupon, CouponAdmin)


