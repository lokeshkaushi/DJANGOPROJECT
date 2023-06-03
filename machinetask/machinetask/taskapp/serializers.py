from. models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    order_name = serializers.CharField(max_length=100)
    order_price = serializers.FloatField()
    order_quantity = serializers.IntegerField(required=False, default=1)
    mobile_no = serializers.IntegerField()
    deliver_to = serializers.CharField(max_length=100)
    class Meta:
        model = Order
        fields = "__all__"