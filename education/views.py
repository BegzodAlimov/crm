from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from education.models import Room, Subject, Level, Course
from education.serializers import RoomSerializer, SubjectSerializer, LevelSerializer, CourseSerializer
from tools.custom_pagination import CustomPagination


class RoomsAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = CustomPagination


class RoomDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SubjectsAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = CustomPagination


class SubjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class LevelsAPIView(ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    pagination_class = CustomPagination


class LevelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class CourseAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination


class CourseDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
