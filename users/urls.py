from django.urls import path
from users.views import UserAPIView, SingleUserAPIView, LoginAPIView, LogoutAPIView, TokenRefreshAPIView, \
    CurrentUserAPIView

urlpatterns = [
    path('', UserAPIView.as_view(), name='users'),
    path('<uuid:pk>/', SingleUserAPIView.as_view(), name='user'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('token/', TokenRefreshAPIView.as_view(), name='token'),
    path('current_user/', CurrentUserAPIView.as_view(), name='current_user'),
]