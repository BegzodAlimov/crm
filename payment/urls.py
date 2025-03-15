from django.urls import path
from payment.views import PaymentsAPIView, PaymentDetailAPIView, DiscountsAPIView, DiscountDetailAPIView

urlpatterns = [
    path('payments/', PaymentsAPIView.as_view(), name='payments'),
    path('payments/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('discounts/', DiscountsAPIView.as_view(), name='discounts'),
    path('discounts/<int:pk>/', DiscountDetailAPIView.as_view(), name='discount-detail'),
]