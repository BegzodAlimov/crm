from drf_yasg import openapi
from users.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from django.db.models.expressions import F, Value
from django.db.models.functions.text import Concat
from tools.custom_pagination import CustomPagination
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserCreateSerializer, UserSerializer, SingleUserSerializer, LoginSerializer, LogoutSerializer, \
    AccessTokenRefreshSerializer

# Create your views here.
class UserAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = CustomPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('page', openapi.IN_QUERY, description="Page number", type=openapi.TYPE_INTEGER),
            openapi.Parameter('page_size', openapi.IN_QUERY, description="Number of items per page",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                'role', openapi.IN_QUERY, description="Filter users by role", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'full_name', openapi.IN_QUERY, description="Filter users by full name", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'gender', openapi.IN_QUERY, description="Filter users by gender", type=openapi.TYPE_STRING
            ),
        ],
        responses={
            200: UserSerializer,
            400: 'Bad Request - Invalid parameters were provided',
            500: 'Internal Server Error - An unexpected error occurred'
        })
    def get(self, request):
        users = User.objects.annotate(
            full_name=Concat(F('first_name'), Value(" "), F('last_name'), Value(" "), F('middle_name'))
        ).only("id",'first_name','last_name', 'middle_name','phone_number', 'status', 'gender').order_by('id')

        role = request.query_params.get('role', None)
        full_name = request.query_params.get('full_name', None)
        gender = request.query_params.get('gender', None)

        if role:
            users = users.filter(role=role)

        if full_name:
            users = users.filter(full_name__icontains=full_name)

        if gender:
            users = users.filter(gender=gender)

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(users, request)

        if page is not None:
            serializer = UserSerializer(page, many=True)

            return paginator.get_paginated_response(serializer.data)

        serializer = UserSerializer(users, many=True)


        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        data = request.data
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserAPIView(APIView):
    serializer_class = SingleUserSerializer
    @swagger_auto_schema(
        responses={
            200: SingleUserSerializer,
            404: 'Not Found - User not found',
            500: 'Internal Server Error - An unexpected error occurred'
        })
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = SingleUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SingleUserAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: SingleUserSerializer,
            404: 'Not Found - User not found',
            500: 'Internal Server Error - An unexpected error occurred'
        })
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound({"message": "Not Found - User not found"})

        serializer = SingleUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=SingleUserSerializer,
                         responses={
            200: SingleUserSerializer,
            404: 'Not Found - User not found',
            500: 'Internal Server Error - An unexpected error occurred'
        })
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound({"message": "Not Found - User not found"})

        serializer = SingleUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={
            204: 'No Content',
            400: 'Bad Request - Invalid parameters were provided',
            500: 'Internal Server Error - An unexpected error occurred'
        })

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound({"message": "Not Found - User not found"})

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer


class LogoutAPIView(APIView):
    serializer_class = LogoutSerializer

    @swagger_auto_schema(
        request_body=LogoutSerializer,
        responses={200: 'Successfully logged out.'}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'success': False, 'message': 'Refresh token not provided.'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            data = {'success': True, 'message': 'Successfully logged out.'}
            return Response(data, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'success': False, 'message': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)


class TokenRefreshAPIView(TokenRefreshView):
    serializer_class = AccessTokenRefreshSerializer
