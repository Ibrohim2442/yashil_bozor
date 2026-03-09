from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']
        read_only_fields = ['price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id', 'recipient_name', 'recipient_phone',
            'courier_note', 'total_price',
            'status', 'items', 'created_at'
        ]
        read_only_fields = ['total_price', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data, user=self.context['request'].user, total_price=0)

        total = 0
        for item in items_data:
            price = item['product'].price
            OrderItem.objects.create(order=order, price=price, **item)
            total += price * item['quantity']

        order.total_price = total
        order.save()
        return order