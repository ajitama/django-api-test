from django.shortcuts import render
from .models import Coupon
from rest_framework import viewsets, filters
from .serializer import CouponSerializer

# Create your views here.

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all() # 全てのデータを取得
    serializer_class = CouponSerializer

