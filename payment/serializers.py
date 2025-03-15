from rest_framework import serializers
from payment.models import Payment, Discount


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "amount", 'student', 'group',  "month",  "payment_type", "payment_date"]


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["id", "amount", 'student', 'group', "month", 'created_by']