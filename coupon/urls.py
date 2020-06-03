from django.urls import path
from . import views
from rest_framework import routers
from .views import CouponViewSet

router = routers.DefaultRouter()
router.register(r'coupon_list', CouponViewSet)
