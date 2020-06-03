from rest_framework import serializers
from .models import Coupon # models.py のcouponクラスをインポート

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon # 扱う対象のモデル名を設定する
        fields = '__all__'
