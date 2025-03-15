from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from payment.models import Payment, Discount
from payment.serializers import PaymentSerializer, DiscountSerializer
from tools.custom_pagination import CustomPagination


# Create your views here.
class PaymentsAPIView(ListCreateAPIView):
    queryset = Payment.objects.all().order_by('-id')
    serializer_class = PaymentSerializer
    pagination_class = CustomPagination


class PaymentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class DiscountsAPIView(ListCreateAPIView):
    queryset = Discount.objects.all().order_by('-id')
    serializer_class = DiscountSerializer
    pagination_class = CustomPagination


class DiscountDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer